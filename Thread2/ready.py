from selenium import webdriver
import random

# random.randint(4700,4900) 生成随机数 4700 - 4900 之前，不包括 4700 4900

class getDeviceInfo(object):

    def get_driver(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '5.1.1',
                        'deviceName': 'msm8916_64',
                        'appPackage': 'com.gwchina.lssw.parent',
                        'noReset' : 'True',  # 去掉，每次启动app都会清除数据
                        'automationName': 'Uiautomator2',
                        'appActivity': 'com.gwchina.tylw.parent.StartEntryActivity'
                        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
