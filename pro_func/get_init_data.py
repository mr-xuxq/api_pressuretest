# -*-coding:utf-8-*-
"""
File Name:get_init_data.py
Program IDE:PyCharm
Create File Time:2022/7/6 3:18 PM
File Create By Author:xuxiaoqi
"""
from conf import read_path
from common.read_config import ReadConfig
from common.do_excel import DoExcel
from common.my_log import MyLog
from conf.read_test_sheet import ReadTestSheet


class GetInitData:

    def get_init_data(self, module_name):
        ip = ReadConfig().read_config(read_path.config_path, 'IP', 'ip')                                                #获取ip地址
        test_sheet = ReadTestSheet().read_test_sheet(module_name)                                                       #通过模块名称来获取表名
        test_excel_path = DoExcel(read_path.test_data_path, test_sheet)                                                 #初始化Excel数据，方便下一步调用方法
        test_excel_data = test_excel_path.do_excel()                                                                    #获取表单数据
        log_name = 'bonree-api-%s'%module_name                                                                          #日志命名
        logger = MyLog(log_name)                                                                                        #初始化日志收集器的名字，方便后面往这个日志里面存放数据
        return ip, test_excel_path, test_excel_data, logger

if __name__ == '__main__':
    List=GetInitData().get_init_data(module_name='test_globalBusinessCollect')
    for s in List:
        print(s)