from Automation_Framework.src.Utilities.requestsUtility import RequestsUtility
import pytest

@pytest.mark.tcid24
def test_get_all_products():
    request_helper = RequestsUtility()
    requests_response = request_helper.get(endpoint='products')
    assert requests_response, f"Get all products endpoint returned nothing."
    return requests_response
