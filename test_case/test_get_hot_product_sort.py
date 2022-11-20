# -*- coding: UTF-8 -*-
from tools.yaml_control import get_yaml_data
import pytest
import os
import allure
from logs.log import log
import time,datetime
import yaml
from configs.config import HOST
from libs.common_post_request import Post_Request


#引入pytest框架
class Test_Get_Hot_Product_Sort:
    # pytest.mark.parametrize调试方法可以遍历返回得所有用例，执行所有用例,用元组对象去接收
    @pytest.mark.parametrize('inBody,expData',get_yaml_data('../data/get_hot_product_sort'))
    def  test_get_hot_product_sort(self,inBody,expData):

        #请求接口地址
        url = f'{HOST}/cockpit-web/product/getHotProductSort'


        #执行请求
        res = Post_Request().post_request(inBody,url)

        #日志引入
        # log.info("-------接口请求开始-----------")
        # log.info("接口名称：getHotProductSort")
        # log.info("请求方式：post")
        # # log.info("用名称为：{}".format(expData['detail']))
        # log.info(f"请求路径：'{HOST}/cockpit-web/product/getHotProductSort'")
        # log.info("请求参数为：{}".format(inBody))
        # log.info("响应结果为：{}".format(res))
        # log.info("响应期望为：{}".format(expData))
        # log.info("-------接口请求结束----------")
        # print()

        #断言判断
        assert res['code'] == expData['code']
        assert res['msg'] == expData['msg']
        assert res['data']['total']>=0

        """
        F 表示用例失败
        E 表示用例错误
        . 表示成功得

        """
if __name__ == '__main__':
    pytest.main(['--clean-alluredir',"test_get_hot_product_sort.py","-s",'--alluredir','../report/tmp'])#   -s打印输出
    os.system("allure serve ../report/tmp")