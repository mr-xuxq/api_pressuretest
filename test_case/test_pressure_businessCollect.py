# -*-coding:utf-8-*-
"""
File Name:test_pressure_businessCollect.py
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
class Test_pressure_BusinessCollect:
    def test_pressure_globalBusinessCollect(self):
        with allure.step('通过模块名称,获取请求数据'):
            ip, test_excel_path, test_excel_data, logger = GetInitData().get_init_data("test_globalBusinessCollect")
        with allure.step("并发结果输出，同步到Excel文件中"):
            PublicTestHttpRequest(ip, test_excel_data, test_excel_path, logger).api_pressuretest()

    def test_pressure_aloneBusinessCollect(self):
        with allure.step('通过模块名称,获取请求数据'):
            ip, test_excel_path, test_excel_data, logger = GetInitData().get_init_data("test_aloneBusinessCollect")
        with allure.step("并发结果输出，同步到Excel文件中"):
            PublicTestHttpRequest(ip, test_excel_data, test_excel_path, logger).api_pressuretest()

if __name__ == "__main__":
    Test_pressure_BusinessCollect().test_pressure_aloneBusinessCollect()

