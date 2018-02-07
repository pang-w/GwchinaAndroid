__author__ = 'Never deter till tomorrow that which you can do today. _20180131'
# -*- coding: utf-8 -*-
import os
import yaml
from run_all import runAllTest2
from multiprocessing import Pool


absPath = os.path.dirname(os.path.abspath('.'))

def getYam(homeyaml):
    try:
        with open(homeyaml, encoding='utf-8') as f:
            x = yaml.load(f)
            print(x)
            return x
    except FileNotFoundError:
        print(u"找不到文件")
def get_devices():
    return getYam(absPath + '\\run_all\\devices.yaml')
ga = get_devices()

def runnerPool():
    devices_Pool = []
    for i in range(0, len(ga["appium"])):
        l_pool = []
        t = {}
        t["deviceName"] = ga["appium"][i]["devices"]
        # t["platformVersion"] = phoneBase.get_phone_info(devices=ga["appium"][i]["devices"])["release"]
        t["platformName"] = ga["appium"][i]["platformName"]
        t["port"] = ga["appium"][i]["port"]
        l_pool.append(t)
        devices_Pool.append(l_pool)
        print(l_pool)
    pool = Pool(len(devices_Pool))
    # for i in range(2):
    #     pool.apply_async(sample_request, args=(t[i],)) # 异步
    pool.map(runAllTest2.writeHtml(), devices_Pool)
    pool.close()
    pool.join()


if __name__ == '__main__':

    # runAllTest2.Creatsuite()
    # runAllTest2.writeHtml()
    runnerPool()