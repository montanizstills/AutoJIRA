import json
import os
import unittest

from requests.auth import HTTPBasicAuth

from src.main import issue


class IssueTest(unittest.TestCase):
    def setUp(self):
        self.jira_auth_email = os.environ.get("JIRA_AUTH_EMAIL") if os.environ.get("JIRA_AUTH_EMAIL") else \
            json.load(open('../../resources/jira-credentials.json'))['jira_auth_email']
        self.token = os.environ.get("JIRA_API_KEY") if os.environ.get("JIRA_API_KEY") else \
            json.load(open('../../resources/jira-credentials.json'))['jira_api_key']
        self.url = os.environ.get("JIRA_URL") if os.environ.get(
            "JIRA_URL") else f"{json.load(open('../../resources/jira-credentials.json'))['jira_url']}/rest/api/2/issue/"
        self.basic_auth = HTTPBasicAuth(self.jira_auth_email, self.token)
        self.headers = {
            "Content-Type": "application/json",
        }

    def doClassCleanups(self) -> None:
        # clean up board after all tests
        # clean up after create
        # clean up after read
        # clean up after update
        pass

    def test_create_issue(self):
        # create story
        # create bug
        # create epic
        # create subtask

        # given
        data = {
            "fields": {
                "project": {
                    "key": "SAGC"
                },
                "summary": "Test Issue - Create_for_Read_Test",
                "description": "This issue is created to be read, then deleted.",
                "issuetype": {
                    "name": "Story"  # case-sensitive
                }
            }
        }

        # when
        response = issue.create_issue(self.url, self.headers, self.basic_auth, data).json()

        # then
        self.assertTrue(response.get('id'))
        self.assertTrue(response.get('key'))
        self.assertTrue(response.get('self'))

    def test_read_issue(self):
        # positive test for when issue exists
        # given
        data = {
            "fields": {
                "project": {
                    "key": "SAGC"
                },
                "summary": "Issue summary2",
                "description": "Issue description",
                "issuetype": {
                    "name": "Story"
                }
            }
        }

        # when
        response = issue.create_issue(self.url, self.headers, self.basic_auth, data).json()
        issue_key = response.get('key')
        response = issue.read_issue(self.url, self.headers, self.basic_auth, issue_key).json()

        # then
        self.assertEqual('Story', response.get('fields').get('issuetype').get('name'))
        self.assertIn(data.get('fields').get('project').get('key'), response.get('key'))

        # negative test for when issue does not exist
        # TODO

    def test_update_issue(self):
        # positive test for when issue exists
        # given
        start = {
            "fields": {
                "project": {
                    "key": "SAGC"
                },
                "summary": "Test Issue - Updated - Start",
                "description": "This is the description when the issue is first created",
                "issuetype": {
                    "name": "Story"
                }
            }
        }
        end = {
            "fields": {
                "project": {
                    "key": "SAGC"
                },
                "summary": "Test Issue - Updated - End",
                "description": "This is the description after the issue has been updated.",
                "issuetype": {
                    "name": "Bug"
                }
            }
        }

        # when
        issue_key = issue.create_issue(self.url, self.headers, self.basic_auth, start).json().get('key')
        issue.update_issue(self.url, self.headers, self.basic_auth, issue_key, end)
        updated_issue_json = issue.read_issue(self.url, self.headers, self.basic_auth, issue_key).json()

        # then
        self.assertEqual(end.get('description'), updated_issue_json.get('description'),
                         f"Expected {end.get('description')}, but got {updated_issue_json.get('description')}")

        # negative test for when issue does not exist
        # TODO

    def test_delete_issue(self):
        # positive test for when issue exists
        # given
        data = {
            "fields": {
                "project": {
                    "key": "SAGC"
                },
                "summary": "Test Issue - to be deleted",
                "description": "This is the description of an issue you will never see.",
                "issuetype": {
                    "name": "Story"
                }
            }
        }

        # when
        response = issue.create_issue(self.url, self.headers, self.basic_auth, data).json()
        issue_key = response.get('key')
        delete_response = issue.delete_issue(self.url, self.headers, self.basic_auth, issue_key)
        error_json = issue.read_issue(self.url, self.headers, self.basic_auth, issue_key).json()

        # then
        assert delete_response.status_code == 204
        assert 'Issue does not exist or you do not have permission to see it.' in error_json.get('errorMessages')


if __name__ == "__main__":
    unittest.main()
