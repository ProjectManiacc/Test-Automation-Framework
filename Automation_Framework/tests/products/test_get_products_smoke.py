from Automation_Framework.src.Utilities.requestsUtility import RequestsUtility
from Automation_Framework.src.dao.products_dao import ProductsDAO
from Automation_Framework.src.helpers.products_helper import ProductsHelper
import pytest

pytestmark = [pytest.mark.smoke]
@pytest.mark.products
@pytest.mark.tcid24
def test_get_all_products():
    request_helper = RequestsUtility()
    requests_response = request_helper.get(endpoint='products')
    assert requests_response, f"Get all products endpoint returned nothing."


@pytest.mark.products
@pytest.mark.tcid25
def test_get_product_by_id():
    product_obj = ProductsDAO()
    random_product = product_obj.get_random_product_from_db()
    random_product_id = random_product[0]['ID']
    random_product_name = random_product[0]['post_title']

    product_helper = ProductsHelper()
    api_response = product_helper.get_product_by_id(random_product_id)
    api_response_product_name = api_response['name']

    assert api_response, f'Get product by ID returned nothing'
    assert random_product_name == api_response_product_name, f"Get product by ID returned wrong product. " \
                                                             f"ID={random_product_id}. Random_product_name:" \
                                                             f" {random_product_name}. Api_response_product_name: " \
                                                             f"{api_response_product_name} "
