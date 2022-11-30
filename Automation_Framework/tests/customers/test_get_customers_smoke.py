from Automation_Framework.src.Utilities.requestsUtility import RequestsUtility
import pytest
import logging as logger

@pytest.mark.customers
@pytest.mark.tcid30
def test_get_all_customers():
    requests_helper = RequestsUtility()
    requests_response = requests_helper.get('customers')
    assert requests_response, f"Response for the list of all customers is empty"

