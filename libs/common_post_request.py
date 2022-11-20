import requests
from configs.config import HOST,headers
import hashlib,urllib3
from urllib import parse


class Post_Request:
    def post_request(self,data,url):
        urllib3.disable_warnings()
        resp = requests.post(url=url, json=data, headers=headers, verify=False)
        return resp.json()