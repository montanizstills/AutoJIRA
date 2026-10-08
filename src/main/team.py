import requests


def create_team(url, headers, auth, org_id, data):
    url = f"{url}/gateway/api/public/teams/v1/org/{org_id}/teams/"
    return requests.post(url,
                         json=data,
                         headers=headers,
                         auth=auth
                         )


def read_team(url, headers, auth, org_id, team_id):
    return requests.get(f"{url}/gateway/api/public/teams/v1/org/{org_id}/teams/{team_id}",
                        headers=headers,
                        auth=auth
                        )


def update_team(url, headers, auth, org_id, team_id, data):
    return requests.patch(f"{url}/gateway/api/public/teams/v1/org/{org_id}/teams/{team_id}",
                          json=data,
                          headers=headers,
                          auth=auth
                          )


def delete_team(url, headers, auth, org_id, team_id):
    return requests.delete(f"{url}//gateway/api/public/teams/v1/org/{org_id}/teams/{team_id}",
                           headers=headers,
                           auth=auth
                           )


def read_all_team_members(url, headers, auth, org_id, team_id):
    return requests.post(f"{url}/gateway/api/public/teams/v1/org/{org_id}/teams/{team_id}/members",
                         headers=headers,
                         auth=auth
                         )


def add_all_team_members(url, headers, auth, org_id, team_id, data):
    return requests.post(f"{url}/gateway/api/public/teams/v1/org/{org_id}/teams/{team_id}/members/add",
                         json=data,
                         headers=headers,
                         auth=auth,
                         )


def delete_all_team_members(url, headers, auth, org_id, team_id, data):
    return requests.post(f"{url}/gateway/api/public/teams/v1/org/{org_id}/teams/{team_id}/members/remove",
                         json=data,
                         headers=headers,
                         auth=auth
                         )
