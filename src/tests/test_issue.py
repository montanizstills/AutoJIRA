from src.main import issue


def test_create_issue(url, headers, basic_auth):
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
            "summary": "Test Issue - Create",
            "description": "This issue is created to unit test issue.create_issue.",
            "issuetype": {
                "name": "Story"  # case-sensitive
            }
        }
    }

    # when
    response = issue.create_issue(url, headers, basic_auth, data).json()

    # then
    assert response.get('id')
    assert response.get('key')


def test_read_issue(url, headers, basic_auth):
    # positive test for when issue exists
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
    expected = data.get('fields').get('project').get('key')

    # when
    response = issue.create_issue(url, headers, basic_auth, data).json()
    issue_key = response.get('key')
    response = issue.read_issue(url, headers, basic_auth, issue_key).json()

    # then
    actual = response.get('key')
    assert 'Story' == response.get('fields').get('issuetype').get('name')
    assert expected in actual, f"Expected {expected}, but got {actual}"

    # negative test for when issue does not exist
    # TODO


def test_update_issue(url, headers, basic_auth):
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
    expected = end.get('description')

    # when
    issue_key = issue.create_issue(url, headers, basic_auth, start).json().get('key')
    issue.update_issue(url, headers, basic_auth, issue_key, end)
    updated_issue_json = issue.read_issue(url, headers, basic_auth, issue_key).json()
    actual = updated_issue_json.get('description')

    # then
    assert expected == actual, f"Expected {expected}, but got {actual}"

    # negative test for when issue does not exist
    # TODO

def test_delete_issue(url, headers, basic_auth):
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
    response = issue.create_issue(url, headers, basic_auth, data).json()
    issue_key = response.get('key')
    delete_response = issue.delete_issue(url, headers, basic_auth, issue_key)
    error_json = issue.read_issue(url, headers, basic_auth, issue_key).json()

    # then
    assert delete_response.status_code == 204
    assert 'Issue does not exist or you do not have permission to see it.' in error_json.get('errorMessages')
