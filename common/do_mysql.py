# -*-coding:utf-8-*-
"""
File Name:do_mysql.py
Program IDE:PyCharm
Create File Time:2022/7/4 3:18 PM
File Create By Author:xuxiaoqi
"""
from mysql import connector
from conf import read_path
from common.read_config import ReadConfig

class DoMysql:
    def __init__(self):
        self.config=eval(ReadConfig().read_config(read_path.config_path, 'DB', 'config'))

    def do_mysql(self, query, state=0):
        try:
            # 1.连接数据库
            cnn=connector.connect(**self.config)
            # 2.创建游标对象
            cur = cnn.cursor()
            # 3对数据库进行增删改查，执行sql语句
            cur.execute(query)
            if state == 0:
                result = cur.fetchone()
            else:
                result = cur.fetchall()
            # 4.关闭游标
            cur.close()
            # 5.关闭数据库连接
            cnn.close()
            return result

            # 可能会抛出异常
        except Exception as err:
            print('Error: {}'.format(err))


if __name__ == "__main__":
    period = DoMysql().do_mysql(r'SELECT * from t_srv_acc WHERE account_name = "apm_test" AND `status`=1 ORDER BY create_date DESC')[0]
    print(period)
