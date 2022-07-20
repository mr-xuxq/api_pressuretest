#-*-coding:utf-8-*-
"""
File Name:public_test_http_request.py
Program IDE:PyCharm
Create File Time:2022/7/6 3:18 PM
File Create By Author:xuxiaoqi
"""
import allure
from common.http_request import HttpRequest
from pro_func.get_init_data import GetInitData
test_dict={}

class PublicTestHttpRequest:
    def __init__(self, ip, test_excel_data, test_excel_path, logger):
        self.ip = ip
        self.test_excel_data = test_excel_data
        self.test_excel_path = test_excel_path
        self.logger = logger

    def send_request(self):
        for i in self.test_excel_data:  # 将列表转换成字典
            test_dict.update(i)
            res = HttpRequest().http_request(url=self.ip + test_dict["url"],param=eval(test_dict["param"]),method=test_dict["method"])
            try:
                if res.status_code == 200:
                    with allure.step(test_dict["case_name"] + '接口的响应时间是：' + str(res.elapsed.microseconds / 1000) + 'ms'):
                        self.test_excel_path.write_data(test_dict['case_id'] + 1, 10, str(res.elapsed.microseconds / 1000) + 'ms')
                        self.test_excel_path.write_data(test_dict['case_id'] + 1, 11, 1)
                else:
                    with allure.step(test_dict["case_name"] + '接口响应异常，请检查环境'):
                        self.test_excel_path.write_data(test_dict['case_id'] + 1, 10, str(res.elapsed.microseconds / 1000) + 'ms')
                        self.test_excel_path.write_data(test_dict['case_id'] + 1, 11, 1)
            except Exception as e:
                pass
            self.test_excel_path.write_data(test_dict['case_id'] + 1, 8, str(res.json()))
            self.test_excel_path.write_data(test_dict['case_id'] + 1, 11, 1)

    def api_pressuretest(self):
        for i in self.test_excel_data:  # 将列表转换成字典
            test_dict.update(i)
            try:
                if test_dict["concurrency"] == None or test_dict["cycles"] == None:
                    print('错误：您未设置并发数和循环次数')
            except Exception as e:
                pass
            pressure_result = HttpRequest().run(test_dict["case_name"],press_url=self.ip + test_dict["url"], param=eval(test_dict["param"]), THREAD_NUM=test_dict["concurrency"],ONE_WORKER_NUM=test_dict["cycles"])
            self.test_excel_path.write_data(test_dict['case_id'] + 1, 10, pressure_result[2])
            self.test_excel_path.write_data(test_dict['case_id'] + 1, 11, test_dict["concurrency"])
            self.test_excel_path.write_data(test_dict['case_id'] + 1, 12, test_dict["cycles"])
            self.test_excel_path.write_data(test_dict['case_id'] + 1, 13, pressure_result[1])
            self.test_excel_path.write_data(test_dict['case_id'] + 1, 14, pressure_result[3])

    def assert_result(self):
        for i in self.test_excel_data:  # 将列表转换成字典
            test_dict.update(i)
            res = HttpRequest().http_request(url=self.ip + test_dict["url"], param=eval(test_dict["param"]),method=test_dict["method"])
            try:
                test_result = 'unknow'
                assert res.status_code == 200
                assert eval(test_dict["expected_1"])
                assert eval(test_dict["expected_2"])
                test_result = 'PASS'
                with allure.step(test_dict["case_name"] + '接口的响应结果为：' + test_result):
                    self.test_excel_path.write_data(i['case_id'] + 1, 9, test_result)  # 保存测试结果
            except AssertionError as e:
                self.logger.error("执行用例{0}的时候报错:{1}".format(test_dict["case_id"], e))
                self.logger.info("预期结果是：{0}；实际请求结果是:{1}".format(test_dict["expected_2"], self.send_request()))
                test_result = 'FAIL'
                with allure.step(test_dict["case_name"] + '接口的响应结果为：' + test_result):
                    self.test_excel_path.write_data(i['case_id'] + 1, 9, test_result)  # 保存测试结果

if __name__ == '__main__':
    ip, test_excel_path, test_excel_data, logger = GetInitData().get_init_data("test_globalBusinessCollect")
    #res=PublicTestHttpRequest(ip, test_excel_data, test_excel_path, logger).send_request()
    PublicTestHttpRequest(ip, test_excel_data, test_excel_path, logger).api_pressuretest()
    #PublicTestHttpRequest(ip, test_excel_data, test_excel_path, logger).assert_result()
    #print(res)

