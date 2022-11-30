from Automation_Framework.src.Utilities.dbUtility import DBUtility

class CustomersDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self,email):

        sql = f"SELECT * FROM local.wp_users WHERE user_email = '{email}';"

        response_sql = self.db_helper.execute_select(sql)
        return response_sql

    def get_random_customer_from_db(self, quantity=1):

        sql = f"SELECT * FROM local.wp_users ORDER BY rand() LIMIT {quantity};"
        response_sql = self.db_helper.execute_select(sql)

        return response_sql

