#-*-coding:utf-8-*-
"""
File Name:read_config.py
Program IDE:PyCharm
Create File Time:2022/7/4 3:18 PM
File Create By Author:xuxiaoqi
"""
import configparser
# 专门读取配置文件的类

class ReadConfig:
    def read_config(self, conf_file, section, option):
        cf = configparser.ConfigParser()
        cf.read(conf_file, encoding='utf-8')
        value = cf.get(section, option)
        # section 片段 option 选项 value 值
        return value

if __name__ == '__main__':
    from conf import read_path
    conf_file = read_path.config_path
    value = ReadConfig().read_config(conf_file, 'IP', 'ip')
    print(conf_file,'\n',value)