from Automation_Framework.src.Utilities.requestsUtility import RequestsUtility
import logging as logger


class ProductsHelper(object):

    def __init__(self):

        self.requests_helper = RequestsUtility()

    def get_product_by_id(self, product_id):
        return self.requests_helper.get(endpoint=f"products/{product_id}")

    def create_product(self, name, price, type='simple', **kwargs):

        payload = dict()
        payload['name'] = name
        payload['type'] = type
        payload['regular_price'] = price
        payload.update(kwargs)
        create_product_json = self.requests_helper.post(endpoint='products', payload=payload, expected_status_code=201)
        return create_product_json

    def list_all_products(self, payload=None):

        max_pages = 1000
        all_products = []
        for i in range(1, max_pages + 1):
            logger.debug(f"List products page number:{i}")

            if 'per_page' not in payload.keys():
                payload['per_page'] = 100

            payload['page'] = i
            api_response = self.requests_helper.get(endpoint='products', payload=payload)

            if not api_response:
                break
            else:
                all_products.extend(api_response)
        else:
            raise Exception(f'Unable to find all products after {max_pages} pages.')

        return all_products
