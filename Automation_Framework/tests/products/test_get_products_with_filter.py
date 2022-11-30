from Automation_Framework.src.helpers.products_helper import ProductsHelper
from Automation_Framework.src.dao.products_dao import ProductsDAO
from datetime import datetime, timedelta
import pytest
@pytest.mark.regression
class TestListProductsWithFilter(object):

    @pytest.mark.tcid51
    def test_list_products_with_filter_after(self):

        x_days_from_today = 30
        payload = dict()
        payload['after'] = (datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)).isoformat()

        products_helper = ProductsHelper()
        api_response = products_helper.list_all_products(payload=payload)
        assert api_response, f"Empty response for 'list products with filter'"

        products_dao = ProductsDAO()
        products_in_db = products_dao.get_product_created_after_given_data(payload['after'])

        assert len(api_response) == len(products_in_db), f"Number of products in API is different than in DB" \
                                                         f"API: {len(api_response)}, DB: {len(products_in_db)}"

        ids_in_api = [i['id'] for i in api_response]
        ids_in_db = [i['ID'] for i in products_in_db]

        assert ids_in_api[::-1] == ids_in_db, f'IDs in API did not match IDs in DB.' \
                                        f'API: {ids_in_api}, DB: {ids_in_db}'