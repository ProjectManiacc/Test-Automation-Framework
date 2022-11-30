from Automation_Framework.src.helpers.products_helper import ProductsHelper
from Automation_Framework.src.Utilities.genericUtilities import generate_random_string
from Automation_Framework.src.dao.products_dao import ProductsDAO
import pytest

@pytest.mark.products
@pytest.mark.tcid26
def test_create_one_simple_product():

    product_helper = ProductsHelper()
    random_name = generate_random_string()

    created_product = product_helper.create_product(name=random_name, price='99.99')

    assert created_product, f"Created product, Api response is empty."
    assert created_product['name'] == random_name, f"Created product, Api response has an unexpected name" \
                                                   f".Expected: {random_name}, Actual: {created_product['name']}"

    created_product_id = created_product['id']

    product_dao = ProductsDAO()
    product_in_db = product_dao.get_product_by_id_from_db(created_product_id)

    assert product_in_db[0]['post_title'] == created_product['name'], f"Created product, Name in db does not match" \
                                                       f" name in API. DB: {product_in_db[0]['post_title']}," \
                                                                      f" API: {created_product['name']}"

