import requests


def create_issue(url, headers, auth, data):
    return requests.post(url, json=data, headers=headers, auth=auth)


def read_issue(url, headers, auth, issue_key):
    return requests.get(f"{url}/{issue_key}", headers=headers, auth=auth)


def update_issue(url, headers, auth, issue_key, data):
    return requests.put(f"{url}/{issue_key}", json=data, headers=headers, auth=auth)


def delete_issue(url, headers, auth, issue_key):
    return requests.delete(f"{url}/{issue_key}", headers=headers, auth=auth)
