import requests


def get_organization_id(url, headers, auth):
    return requests.get(url, headers, auth)

