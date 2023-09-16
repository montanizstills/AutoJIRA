import httpx
import requests
import json

from requests.auth import HTTPBasicAuth


def create_issue(url, data, headers, auth):
    response = requests.post(url, json=data, headers=headers, auth=auth)
    return response


if __name__ == "__main__":
    jira_auth_email = "stillsassetrecovery@gmail.com"
    api_token = json.load(open('resources/jira-credentials.json'))['jira_api_key']
    url = 'https://stillsassetglobal.atlassian.net/rest/api/2/issue/'
    basic_auth = HTTPBasicAuth(jira_auth_email, api_token)
    headers = {
        "Content-Type": "application/json",
    }
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

    response = create_issue(url, data, headers, basic_auth)
    print(response.status_code)
    print(response.text)
