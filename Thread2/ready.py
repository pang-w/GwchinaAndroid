from selenium import webdriver
import random

# random.randint(4700,4900) ��������� 4700 - 4900 ֮ǰ�������� 4700 4900

class getDeviceInfo(object):

    def get_driver(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '5.1.1',
                        'deviceName': 'msm8916_64',
                        'appPackage': 'com.gwchina.lssw.parent',
                        'noReset' : 'True',  # ȥ����ÿ������app�����������
                        'automationName': 'Uiautomator2',
                        'appActivity': 'com.gwchina.tylw.parent.StartEntryActivity'
                        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
