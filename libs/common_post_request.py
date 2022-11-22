import requests
from configs.config import HOST,headers
import hashlib,urllib3
from urllib import parse


class Request_Type:
    def request_type(self,url,method,json):
        urllib3.disable_warnings()
        # resp = requests.post(url=url, json=data, headers=headers, verify=False)
        resp = requests.request(url,method,json=json,headers=headers, verify=False)
        return resp.json()