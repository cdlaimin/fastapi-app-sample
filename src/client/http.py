import json
import time
import requests
import aiohttp
import urllib3
from src.utils.log_init import logger_loguru as logger

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DEFAULT_TIMEOUT = 300
DEFAULT_RETRY_TIME = 3
DEFAULT_VALID_HTTP_CODE = [200]


class HttpClient(object):

    def base_http(self, url, method, payload, headers, params=None, max_retry_times=DEFAULT_RETRY_TIME,
                  timeout=DEFAULT_TIMEOUT, valid_http_code=DEFAULT_VALID_HTTP_CODE):
        resp_result = None
        payload = json.dumps(payload)
        current_retry_times = 0
        while current_retry_times < max_retry_times:
            try:
                logger.info(
                    'method= {} headers={} payload = {} url= {} params= {}'.format(method, headers, payload, url,
                                                                                   params))
                resp = requests.request(
                    method=method, url=url, data=payload, headers=headers, params=params, verify=False, timeout=timeout)
                if resp.status_code in valid_http_code:
                    resp_result = json.loads(resp.text)
                    logger.info('url= {} resp_result {}'.format(url, resp_result))
                    break
                else:
                    current_retry_times += 1
                    logger.error('Retrying: job - request code ={} and msg = {} url={}'.format(
                        repr(resp.status_code), resp.text, url))
            except Exception as e:
                logger.error(e)
                current_retry_times += 1
            time.sleep(2)
        return resp_result

    async def async_http_get(self, url, headers):
        async with aiohttp.ClientSession() as session:
            try:
                logger.info('method= async_http_get headers ={} url= {}'.format(headers, url))
                async with session.get(url=url, headers=headers, ssl=False) as response:
                    return {**(await response.json(content_type=None)), 'url': url}
            except aiohttp.ClientError as e:
                logger.error(e)
                return {}

    async def async_http_post(self, url, payload, headers):
        payload = json.dumps(payload)
        async with aiohttp.ClientSession() as session:
            try:
                logger.info('method= async_http_post headers ={} payload = {} url= {}'.format(headers, payload, url))
                async with session.post(url=url, headers=headers, ssl=False, data=payload) as response:
                    return {**(await response.json(content_type=None)), 'url': url, 'payload': json.loads(payload)}
            except aiohttp.ClientError as e:
                logger.error(e)
                return {}

    async def async_http_put(self, url, payload, headers):
        payload = json.dumps(payload)
        async with aiohttp.ClientSession() as session:
            try:
                logger.info('method= async_http_post headers ={} payload = {} url= {}'.format(headers, payload, url))
                async with session.put(url=url, headers=headers, ssl=False, data=payload) as response:
                    return {**(await response.json(content_type=None)), 'url': url, 'payload': json.loads(payload)}
            except aiohttp.ClientError as e:
                logger.error(e)
                return {}
