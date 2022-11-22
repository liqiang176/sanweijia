import pytest
import os
import allure
from logs.log import log
import time,datetime
import yaml
from configs.config import HOST
from libs.common_post_request import Request_Type
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

url = "https://magiccube-gateway.3vjia.com/sso-plus/lgr/passLogin"
headers =  {'Content-Type': 'application/x-www-form-urlencoded',
           'cookie': 'V-LOGGER-UUID=2fcfd1ae-e192-4a21-8ead-d24a8535af7d; Hm_lvt_53875caa88bd0e3b344ac7ded73448c3=1667549788; Qs_lvt_304777=1667549788; Qs_pv_304777=153144781218764600; sensorsdata2015jssdkcross={"distinct_id":"1000473786","first_id":"18441b6776efce-04c004aa7924e2-f791539-1600000-18441b6776f107a","props":{"$latest_traffic_source_type":"直接流量","$latest_search_keyword":"未取到值_直接打开","$latest_referrer":""},"$device_id":"18441b6776efce-04c004aa7924e2-f791539-1600000-18441b6776f107a"}; SWJ_SSO_SESSION_ID=338422fb77514d118a40882470fbd9d5; is_authed=1; JSESSIONID=579BA34AB22765BC27A8EDA7AE44089D'.encode('utf-8').decode('latin-1')
           }
data = {
'account': 'mnkkadmin',
'password': 'ZYbgxlO3Wy5j+xhJVjm2ouFXdUbnvymGi0VhltYaDo0o7/rdpXIyuooK+6JFmbpMIGkGWlCr6hHGw4M/5EpdortpTtCEV+OZyyHh30m6mTxTEMdrqnPgCL3VhXkdp8ZoH3rHyQHxu12FT9rs0iX2IMOzskLtD/i8JtqFLfsLk7s=',
'clientId': False,
'appId': 'svj-work-main-pc'
}
resp = requests.post()
Token = resp.headers.get("set-cookie")
print(Token)
print(resp.text)