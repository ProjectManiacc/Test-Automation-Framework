import pytest

@pytest.fixture(scope='module')
def my_setup():
    print("")
    print(">>>> My Setup <<<<")

    return {'id': 'JOHN'}

@pytest.mark.smoke
def test_login_page_valid_user(my_setup):
    print('Login as a valid user')
    print('Function: A')
    print(f'Id for setup: {my_setup.get("id")}')

@pytest.mark.regression
def test_login_page_wrong_password(my_setup):
    print('Login with wrong password')
    print('Function: B')
    # assert 1==2, "One is not two"
