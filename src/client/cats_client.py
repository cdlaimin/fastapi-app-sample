from configparser import ConfigParser
from src.client.http import HttpClient

config = ConfigParser()
config.read('config.ini')
CAT_HOST = config.get('ENDPOINT', 'CAT_HOST')
http_client = HttpClient()


class CatClient(object):
    def __init__(self):
        pass

    def get_all_tags(self):
        method = "GET"
        url = '{}/api/tags'.format(CAT_HOST)
        payload = {}
        headers = {
            'Accept': "application/json",
            'Content-type': "application/json"
        }
        return_result = None
        resp_result = http_client.base_http(url=url, method=method, payload=payload, headers=headers)
        if resp_result:
            return_result = resp_result
        return return_result
