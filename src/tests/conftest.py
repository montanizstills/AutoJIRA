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
    return os.environ.get("JIRA_URL")


@pytest.fixture(scope='session')
def basic_auth():
    auth_email = os.environ.get("JIRA_AUTH_EMAIL")

    token = os.environ.get("JIRA_API_KEY")

    return HTTPBasicAuth(auth_email, token)
