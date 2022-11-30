from Automation_Framework.src.Utilities.credentialsUtility import CredentialsUtility
import pymysql
import logging as logger

class DBUtility(object):

    def __init__(self):
        credentials_helper = CredentialsUtility()
        self.credentials = credentials_helper.get_db_credentials()
        self.host = 'localhost'

    def create_connection(self):
        connection = pymysql.connect(host=self.host, user=self.credentials['DB_USER'],
                                     password=self.credentials['DB_PASSWORD'], port=10005)
        return connection

    def execute_select(self, sql):
        conn = self.create_connection()
        try:
            logger.debug(f"Executing sql: {sql}")
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            query_response = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed to execute sql query: {sql} \n Error:{str(e)}")
        finally:
            conn.close()

        return query_response

    def execute_sql(self, sql):
        pass
