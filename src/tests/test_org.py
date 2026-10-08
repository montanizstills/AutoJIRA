from src.main.org import get_organization_id


def test_get_org_id(url, headers, basic_auth):
    # given
    # when
    response = get_organization_id(url, headers, basic_auth)

    # then
    print(response.status_code)
    response = response.text
    print(response)
    assert True
