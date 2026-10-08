import requests


def get_organization_id(url, headers, auth):
    return requests.get(f"{url}/rest/api/3/organization/self", headers, auth=auth)

