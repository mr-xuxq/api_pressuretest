#-*-coding:utf-8-*-
"""
File Name:read_yaml_data.py
Program IDE:PyCharm
Create File Time:2022/7/6 3:18 PM
File Create By Author:xuxiaoqi
"""
import yaml,random

class ReadYamlData:
    def read_yaml_data(self, yaml_file_path):
        with open(yaml_file_path, "r", encoding="utf-8") as f:
            data = f.read()
            yaml_reader = yaml.load(data, Loader=yaml.Loader)
            return yaml_reader["test_uid"]

if __name__ == "__main__":
    from conf import read_path
    yaml_data = ReadYamlData().read_yaml_data(read_path.yaml_file_path)
    random_uid = ReadYamlData().read_yaml_data(read_path.yaml_file_path)[random.randint(0, 4)]
    print(yaml_data)
    print(random_uid)
