import requests
import json


def invite_user(url, headers, auth, email):
    return requests.post(url, json=json.dumps(email), headers=headers, auth=auth)
