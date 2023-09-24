from src.main.team import read_team, create_team, read_all_team_members


def test_create_team(url, headers, basic_auth, org_id):
    # given
    data = {
        'description': "A team created via the Team API",
        'displayName': "TEAM-A1",
        'teamType': "MEMBER_INVITE"
    }

    # when
    response = create_team(url, headers, basic_auth, org_id, data)
    print(response.status_code)
    response = response.json()
    print(response)

    # then
    actual_description = response.get('description')
    expected_description = data.get('description')
    actual_displayName = response.get('displayName')
    expected_displayName = response.get('displayName')
    actual_members = response.get('members')
    expected_members = data.get('members')
    actual_organizationId = response.get('organizationId')
    expected_organizationId = data.get('organizationId')
    actual_teamId = response.get("teamId")
    expected_teamId = data.get("teamId")
    actual_teamType = response.get("teamType")
    expected_teamType = data.get("teamType")
    assert actual_description == expected_description, f"Expected {expected_description}, but got {actual_description}"
    assert actual_displayName == expected_displayName, f"Expected {expected_displayName}, but got {actual_displayName}"
    assert len(actual_members) == len(
        expected_members), f"Expected {expected_members} members, but got {actual_members}"
    assert actual_organizationId == expected_organizationId, f"Expected {expected_organizationId}, but got {actual_organizationId}"
    assert actual_teamId == expected_teamId, f"Expected {expected_teamId}, but got {actual_teamId}"
    assert actual_teamType == expected_teamType, f"Expected {expected_teamType}, but got {actual_teamType}"


def test_read_team(url, headers, basic_auth, org_id):
    # given
    # when
    response = read_all_team_members(url, headers, basic_auth, org_id, "d84ed0dd-e174-473d-883a-6d65b6091e8a")
    print(response.status_code)
    response = response.json()
    print(response)
    # then
    assert True


def test_read_all_team_members(url, headers, basic_auth, org_id):
    # given
    # when
    response = read_all_team_members(url, headers, basic_auth, org_id, "d84ed0dd-e174-473d-883a-6d65b6091e8a")
    print(response.status_code)
    response = response.json()
    print(response)
    # then
    assert True
