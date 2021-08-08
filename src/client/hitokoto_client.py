from configparser import ConfigParser
from src.client.http import HttpClient

config = ConfigParser()
config.read('config.ini')
HITO_HOST = config.get('ENDPOINT', 'HITO_HOST')
http_client = HttpClient()


class HITOClient(object):
    def __init__(self):
        pass

    def get_single_result(self):
        method = "GET"
        url = '{}'.format(HITO_HOST)
        payload = {}
        headers = {
            'Accept': "application/json",
            'Content-type': "application/json"
        }
        query = {'c': 'k'}
        return_result = None
        resp_result = http_client.base_http(url=url, method=method, payload=payload, headers=headers, params=query)
        if resp_result:
            return_result = resp_result
        return return_result
