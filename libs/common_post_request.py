import requests
from configs.config import HOST,headers
import hashlib,urllib3
from urllib import parse


class Request_Type:
    def request_type(self,method,data,url):
        urllib3.disable_warnings()
        # resp = requests.post(url=url, json=data, headers=headers, verify=False)
        resp = requests.request(method=method,url=url,json=data, headers=headers, verify=False)
        return resp.json()