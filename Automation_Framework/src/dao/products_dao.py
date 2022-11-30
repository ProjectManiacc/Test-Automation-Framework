from Automation_Framework.src.Utilities.dbUtility import DBUtility
import random


class ProductsDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, quantity=1):
        sql = f"SELECT * FROM local.wp_posts WHERE post_type = 'product' LIMIT 1000"

        response_sql = self.db_helper.execute_select(sql)

        return random.sample(response_sql, int(quantity))

    def get_product_by_id_from_db(self, id):
        sql = f"SELECT * FROM local.wp_posts WHERE post_type = 'product' AND ID = {id}"

        response_sql = self.db_helper.execute_select(sql)
        return response_sql

    def get_product_created_after_given_data(self,_date):

        sql = f"SELECT * FROM local.wp_posts WHERE post_type = 'product' AND post_date > '{_date}' LIMIT 1000"

        response_sql =self.db_helper.execute_select(sql)
        return response_sql

