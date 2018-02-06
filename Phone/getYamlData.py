__author__ = 'Never deter till tomorrow that which you can do today. _20180131'
# -*- coding: utf-8 -*-
import yaml
import os

abs_path = os.path.dirname(os.path.abspath('.')) + '\\Phone\\devices.yaml'

# -*- coding:utf-8 -*-
def getYaml(homeyaml):
    try:
        with open(homeyaml, encoding='utf-8') as f:
            x = yaml.load(f)
            print(x)
            return x
    except FileNotFoundError:
        print(u"找不到文件")

if __name__ == '__main__':
    getYaml(abs_path)