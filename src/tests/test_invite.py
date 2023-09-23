import json

import requests

from src.main import invite


def test_invite_user(url, headers, basic_auth):
    # given
    url = f"{url}/rest/api/2/user"
    headers['Accept'] = "application/json"
    user_email = {"emailAddress": "montanizstills@gmail.com"}
    # print(headers)

    # when
    response = invite.invite_user(url, headers, basic_auth, json.dumps(user_email))
    print(response)
    print(response.json())
    print(response.status.code)


def test_invite_user_by_email(url, basic_auth):

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "emailAddress": "montanizstills@gmail.com"
    })

    response = requests.post(
        url,
        data=payload,
        headers=headers,
        auth=basic_auth
    )

    print(response.status_code)


def test_get_users(url, basic_auth):
    headers = {
        "Accept": "application/json"
    }

    response = requests.post(
        f"{url}/rest/api/3/users",
        headers=headers,
        auth=basic_auth
    )

    print(response.text)


def test_get_account_id(url, headers, basic_auth):
    import requests

    username = "stillsssetrecovery@gmail.com"

    response = requests.get(f"{url}/rest/api/2/email?email={username}", headers=headers,auth=basic_auth)
    print(response.status_code)
    user_data = response.json()

    print(user_data)
    account_id = user_data["accountId"]
    print(account_id)
