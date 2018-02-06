from selenium import webdriver
from appium import webdriver

class AppiumTest(object):

    def __init__(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '5.1.1',
                        'deviceName': 'msm8916_64',
                        'appPackage': 'com.gwchina.lssw.parent',
                        'noReset' : 'True',  # 去掉，每次启动app都会清除数据
                        'automationName': 'Uiautomator2',
                        'appActivity': 'com.gwchina.tylw.parent.StartEntryActivity'
                        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # self.driver.implicitly_wait(30)

    def get_driver(self):
        return self.driver

class AppiumTestclear(object):

    def __init__(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '5.1.1',
                        'deviceName': 'ZTE B2015',
                        'appPackage': 'com.gwchina.lssw.parent',
                        'automationName': 'Uiautomator2',
                        'appActivity': 'com.gwchina.tylw.parent.StartEntryActivity'
                        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # self.driver.implicitly_wait(30)

    def get_driver(self):
        return self.driver

import os
from testDAL import phoneBase as phone
from testDAL import apkBaseInfo
from testDAL import adbCommon

apkPath = os.path.dirname(os.path.abspath('.')) + '\\ApkData\\GreenBox_Parent_v6.0.0_Nightly_Cs_1801290007.apk'
apk = apkBaseInfo.ApkInfo(apkPath)
device = adbCommon.AndroidDebugBridge().attachedDevices()

class AutoGetPhoneInfo(object):

    def __init__(self):
        desired_caps = {'platformName': 'android',
                        'platformVersion': phone.getPhoneInfo(device)['release'],
                        'deviceName': phone.getPhoneInfo(device)['device'],
                        'appPackage': apk.getApkName(),
                        'automationName': 'Uiautomator2',
                        'appActivity': apk.getApkActivity(),
                        'uuid':'83d7d437'
                        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)

    def get_driver(self):
        return self.driver


import os
from Phone import getYamlData
from testDAL import phoneBase
yamlPath = os.path.dirname(os.path.abspath('.')) + '\\Phone\\devices.yaml'
def get_devices():
    return getYamlData.getYaml(yamlPath)
ga = get_devices()

def runnerPool():
    from multiprocessing import Pool
    devices_Pool = []
    for i in range(0, len(ga["appium"])):
        l_pool = []
        t = {}
        t["deviceName"] = ga["appium"][i]["devices"]
        t["platformVersion"] = phoneBase.getPhoneInfo(devices=ga["appium"][i]["devices"])["release"]
        t["platformName"] = ga["appium"][i]["platformName"]
        t["port"] = ga["appium"][i]["port"]
        l_pool.append(t)
        devices_Pool.append(l_pool)
    pool = Pool(len(devices_Pool))
    # for i in range(2):
    #     pool.apply_async(sample_request, args=(t[i],)) # 异步
    # pool.map(runnerCaseApp, devices_Pool)
    pool.close()
    pool.join()


if __name__ == '__main__':
    # print(phone.getPhoneInfo('83d7d437')['release'])
    # print(phone.getPhoneInfo('83d7d437')['device'])
    # print(phone.getPhoneInfo('83d7d437')['model'])
    # print(phone.getPhoneInfo('83d7d437')['brand'])

    '''
    release = "ro.build.version.release=" # 版本
    model = "ro.product.model=" #型号
    brand = "ro.product.brand=" # 品牌
    device = "ro.product.device=" # 设备名
    '''
