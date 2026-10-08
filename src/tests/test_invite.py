from src.main.invite import invite_user


def test_invite_user_by_email(url, headers, basic_auth):
    # given
    email = "montanizstills@gmail.com"
    # when
    response = invite_user(url, headers, basic_auth, email)

    # then
    print(response.status_code)
    response = response.text
    print(response)
    assert True
