# -*-coding:utf-8-*-
"""
File Name:test_normal_businessCollect.py
Program IDE:PyCharm
Create File Time:2022/7/6 3:18 PM
File Create By Author:xuxiaoqi
"""
import pytest
import allure
from pro_func.get_init_data import GetInitData
from pro_func.public_test_http_request import PublicTestHttpRequest

@allure.feature("业务采集")
@allure.testcase("http://120.133.67.136:8080/business/setting/init?locale=zh_CN",name="业务采集")
class Test_BusinessCollect:
    def test_global_BusinessCollect(self):
        with allure.step('通过模块名称,获取请求数据'):
            ip, test_excel_path, test_excel_data, logger = GetInitData().get_init_data("test_globalBusinessCollect")
        with allure.step("请求响应结果到Excel文件中"):
            PublicTestHttpRequest(ip, test_excel_data, test_excel_path, logger).send_request()
        with allure.step("响应结果断言写入Excel文件中"):
            PublicTestHttpRequest(ip, test_excel_data, test_excel_path, logger).assert_result()

    def test_alone_BusinessCollect(self):
        with allure.step('通过模块名称,获取请求数据'):
            ip, test_excel_path, test_excel_data, logger = GetInitData().get_init_data("test_aloneBusinessCollect")
        with allure.step("请求响应结果到Excel文件中"):
            PublicTestHttpRequest(ip, test_excel_data, test_excel_path, logger).send_request()
        with allure.step("响应结果断言写入Excel文件中"):
            PublicTestHttpRequest(ip, test_excel_data, test_excel_path, logger).assert_result()

if __name__ == "__main__":
    Test_BusinessCollect().test_globalBusinessCollect()

