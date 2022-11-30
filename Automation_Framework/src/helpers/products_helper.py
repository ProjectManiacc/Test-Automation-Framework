from Automation_Framework.src.Utilities.requestsUtility import RequestsUtility

class ProductsHelper(object):

    def __init__(self):

        self.requests_helper = RequestsUtility()

    def get_product_by_id(self,product_id):
        return self.requests_helper.get(endpoint=f"products/{product_id}")