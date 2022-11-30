import pytest
import logging as logger
from Automation_Framework.src.Utilities.genericUtilities import generate_random_email_and_password
from Automation_Framework.src.helpers.customers_helper import CustomerHelper
from Automation_Framework.src.dao.customers_dao import CustomersDAO
from Automation_Framework.src.Utilities.requestsUtility import RequestsUtility


@pytest.mark.customers
@pytest.mark.tcid29
def test_create_customer_only_email_password():
    logger.info("TEST: Create new customer with email and password only")
    rand_info = generate_random_email_and_password()
    email = rand_info['email']
    password = rand_info['password']

    # Make the call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    # Verify email in the response
    assert cust_api_info['email'] == email, f"Create customer api return wrong email. Email: {email}"
    assert cust_api_info[
               'first_name'] == '', f"Create customer api returned value for first_name but it should be empty"

    # Verify customer is created in database
    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)

    # Verify id in API is equal to id in Database
    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID']

    assert id_in_api == id_in_db, f"Created customer response 'id' not the same as 'ID' in database" \
                                  f'Email" {email}'


@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():
    # get existnig email from the database
    cust_dao = CustomersDAO()
    existing_cust = cust_dao.get_random_customer_from_db()
    existing_email = existing_cust[0]['user_email']

    # call the API
    requests_helper = RequestsUtility()
    payload = {'email': existing_email, 'password': 'example123'}
    cust_api_info = requests_helper.post(endpoint='customers', payload=payload, expected_status_code=400)

    assert cust_api_info['code'] == 'registration-error-email-exists', f"Create customer with existing email" \
                                                                       f"user error 'code' is not correct. Expected: 'registration-error-email-exist', Actual: {cust_api_info['code']} "
