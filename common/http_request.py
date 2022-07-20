# -*-coding:utf-8-*-
"""
File Name:http_request.py
Program IDE:PyCharm
Create File Time:2022/7/4 3:18 PM
File Create By Author:xuxiaoqi
"""
import requests,threading,time
from common.my_log import MyLog
from common.read_config import ReadConfig
from conf import read_path
import allure
conf_file = read_path.config_path
logger = MyLog('bonree-api')
headers =eval(ReadConfig().read_config(conf_file, 'HEADERS', 'headers'))

class HttpRequest:
    def http_request(self, url, param, method,cookies={}):
        if method.lower() == 'get':
            try:
                res = requests.get(url,param,headers=headers,cookies=cookies)
            except Exception as e:
                logger.error('请求出错:{0}'.format(e))
                res='Error:get请求报错{0}'.format(e)
        elif method.lower() == 'post':
            try:
                res = requests.post(url, json=param, headers=headers,cookies=cookies)
            except Exception as e:
                logger.error('请求出错:{0}'.format(e))
                res='Error:post请求报错{0}'.format(e)
        else:
            logger.error('你的请求方式错误！')
            res = 'Error:请求方法不对报错{0}'.format(method)
        return res

    def pure_request(self,press_url,param):
        requests.post(press_url, json=param, headers=headers)

    def run(self,case_name,press_url,param,THREAD_NUM,ONE_WORKER_NUM):
        '''使用多线程进程并发测试'''
        t1 = time.time()
        Threads = []

        for i in range(THREAD_NUM):
            t = threading.Thread(self.pure_request(press_url,param))
            t.setDaemon(True)       #通过 t.setDaemon(True) 将子线程设置为守护进程(默认False)，主线程代码执行完毕后，python程序退出，无需理会守护子线程的状态。
            Threads.append(t)

        for t in Threads:
            t.start()
        for t in Threads:
            t.join()                #t.join() 用于阻塞主线程，可以想象成将某个子线程的执行过程插入(join)到主线程的时间线上，主线程的后续代码延后执行。注意和 t.start() 分开写在两个for循环中
        t2 = time.time()

        request_nums=THREAD_NUM * ONE_WORKER_NUM
        total_time=round((t2 - t1)*1000,3)
        average_time=round((t2 - t1) * 1000 / (THREAD_NUM * ONE_WORKER_NUM),3)
        throughput=round(1 / ((t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM)),2)
        with allure.step("==================压测结果======================" ):
            pass
        with allure.step("接口名称：" + case_name):
            pass
        with allure.step("URL:" + press_url):
            pass
        with allure.step("任务数量:{}个".format(request_nums)):
            pass
        with allure.step("总耗时:{:0.3f}ms".format(total_time)):
            pass
        with allure.step("每次请求平均耗时:{:0.3f}ms".format(average_time)):
            pass
        with allure.step("每秒承载请求数:{:0.1f}个".format(throughput)):
            pass
        return request_nums,total_time,average_time,throughput

if __name__=="__main__":
    case_name='获取服务名称'
    ip = ReadConfig().read_config(conf_file, 'IP', 'ip')
    api_path="/plugin/api/business/setting/getClusterNaming"
    url=ip+api_path
    param = {"machineId": 0}
    THREAD_NUM = 5  # 并发线程总数
    ONE_WORKER_NUM = 1  # 每个线程的循环次数
    LOOP_SLEEP = 0.1  # 每次请求时间间隔(秒)
    ERROR_NUM = 0  # 出错数

    '''POST请求示例'''
    res = HttpRequest().http_request(url,param,"post")
    print(str(res.elapsed.microseconds/1000)+'ms')
    print(url)
    print(res.json())
    '''GET请求示例'''
    # get请求时，只需要把param设为None即可
    # res = HttpRequest().http_request("http://www.baidu.com",param=None,method="get")
    # print(res.text)
    '''压测请求示例'''
    # res = HttpRequest().run(case_name,url,param,THREAD_NUM,ONE_WORKER_NUM)
    # print(type(res),res)
    # print(res[0],res[1])