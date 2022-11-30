from Automation_Framework.src.Utilities.requestsUtility import RequestsUtility

class ProductsHelper(object):

    def __init__(self):

        self.requests_helper = RequestsUtility()

    def get_product_by_id(self,product_id):
        return self.requests_helper.get(endpoint=f"products/{product_id}")

    def create_product(self,name,price,type='simple', **kwargs):

        payload = dict()
        payload['name'] = name
        payload['type'] = type
        payload['regular_price'] = price
        payload.update(kwargs)
        create_product_json = self.requests_helper.post(endpoint='products',payload=payload,expected_status_code=201)
        return create_product_json