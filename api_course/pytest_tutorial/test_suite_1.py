import pytest


@pytest.mark.ger
def test_login_page_valid_user():
    print('Login as a valid user')
    print('Function: A')

@pytest.mark.reg
def test_login_page_wrong_password():
    print('Login with wrong password')
    print('Function: B')
    # assert 1==2, "One is not two"
