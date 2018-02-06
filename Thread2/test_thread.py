__author__ = 'Never deter till tomorrow that which you can do today. _20180131'
# -*- coding: utf-8 -*-

import time
import threading
from selenium import webdriver

class AppiumTest1(object):

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

class AppiumTest2(object):

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

def device1():
    for i in range(1):
        AppiumTest1().get_driver()
        time.sleep(1)

def device2():
    for i in range(1):
        AppiumTest1().get_driver()
        time.sleep(1)

threads = []

t1 = threading.Thread(target=device1)
threads.append(t1)

t2 = threading.Thread(target=device2)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        print('start', t)
        t.start()

    for t in threads:
        print('join', t)
        t.join()

    print('end')

