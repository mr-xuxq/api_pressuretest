#-*-coding:utf-8-*-
"""
File Name:read_test_sheet.py
Program IDE:PyCharm
Create File Time:2022/7/6 3:18 PM
File Create By Author:xuxiaoqi
"""
import os

class ReadTestSheet:
    def read_test_sheet(self, module_name):
        if module_name == "test_globalBusinessCollect":
            test_sheet = "business_collect_global"
        elif module_name == "test_aloneBusinessCollect":
            test_sheet = "business_collect_alone"
        else:
            test_sheet = "agent_dowmload"
        return test_sheet