import os

class CredentialsUtility(object):
    def __init__(self):
        pass

    @staticmethod
    def get_wc_api_keys():

        wc_key = os.environ.get('WC_KEY')
        wc_secret = os.environ.get('WC_SECRET')

        if not wc_key or not wc_secret:
            raise Exception('The API credentials "WC_KEY" and "WC_SECRET" must be in environmental variable')
        else:
            return {'WC_KEY': wc_key,'WC_SECRET': wc_secret}

    @staticmethod
    def get_db_credentials():

        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')

        if not db_user or not db_password:
            raise Exception("The DB credentials 'DB_USER' and 'DB_PASSWORD' must be in environmetal variables")
        else:
            return {'DB_USER': db_user, 'DB_PASSWORD': db_password}