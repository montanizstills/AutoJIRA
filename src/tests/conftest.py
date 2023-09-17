import json
import os

import pytest
from requests.auth import HTTPBasicAuth


@pytest.fixture(scope='session')
def headers():
    return {
        "Content-Type": "application/json",
    }


@pytest.fixture(scope='session')
def url():
    if os.environ.get("JIRA_URL"):
        print(os.environ.get("JIRA_URL"))
    else:
        print("No environment variable found for URL")
    return os.environ.get("JIRA_URL") if os.environ.get(
        "JIRA_URL") else f"{json.load(open('../../resources/jira-credentials.json'))['jira_url']}/rest/api/2/issue/"


@pytest.fixture(scope='session')
def basic_auth():
    auth_email = os.environ.get("JIRA_AUTH_EMAIL") if os.environ.get("JIRA_AUTH_EMAIL") else \
        json.load(open('../../resources/jira-credentials.json'))['jira_auth_email']

    print(auth_email)

    token = os.environ.get("JIRA_API_KEY") if os.environ.get("JIRA_API_KEY") else \
        json.load(open('../../resources/jira-credentials.json'))['jira_api_key']

    return HTTPBasicAuth(auth_email, token)
