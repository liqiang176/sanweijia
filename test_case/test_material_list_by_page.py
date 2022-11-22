# -*- coding: UTF-8 -*-
from tools.yaml_control import get_yaml_data
import pytest
import os
import allure
from logs.log import log
import time,datetime
import yaml
from configs.config import HOST
from libs.common_post_request import Request_Type


class Test_Material_list_by_page():
    # pytest.mark.parametrize调试方法可以遍历返回得所有用例，执行所有用例,用元组对象去接收
    @pytest.mark.parametrize("inBody,expData",get_yaml_data('../data/material_list_by_page'))
    def test_material_list_by_page(self,inBody,expData):
        #请求地址
        url = f'{HOST}/workbench-material-web/material/listByPage'

        # 请求方式
        method = "post"

        #请求接口
        resp = Request_Type().request_type(method,url,json=inBody)


        #断言
        assert resp['code'] == expData['code']
        assert resp['msg'] == expData['msg']
        assert resp['data']['total'] >= 1

        #写入日志
        log.info('-----------自动化测试开始-----------')
        log.info("接口地址{}".format(url))
        log.info("接口传值{}".format(inBody))
        log.info("接口实际响应{}".format(resp))
        log.info("接口期望响应{}".format(expData))
        log.info('-----------自动化测试结束-----------')
        print()


if __name__ == '__main__':
    pytest.main(['--clean-alluredir', "test_material_list_by_page.py", "-s", '--alluredir', '../report/tmp'])  # -s打印输出
    # os.system("allure serve ../report/tmp")