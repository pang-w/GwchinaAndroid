from public import Log
from selenium import webdriver
from appium import webdriver
from config import phoneGetConfigInfo

log = Log.Logger(logger='Appium').getLog()
desired_caps = phoneGetConfigInfo.ReadConfig().readDesiredCapsData()
log.critical('desired_caps : (%s) ' % desired_caps)

class Appium(object):

    def __init__(self):
        self.desired_caps = phoneGetConfigInfo.ReadConfig().readDesiredCapsData()

    def driverClear(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': self.desired_caps['platformVersion'],
                        'deviceName': self.desired_caps['deviceName'],
                        'appPackage': self.desired_caps['appPackage'],
                        # 'noReset' : 'True',  # 去掉，每次启动app都会清除数据
                        'automationName': self.desired_caps['automationName'],
                        'appActivity': self.desired_caps['appActivity'],
                        'uuid': self.desired_caps['deviceName'],
                        }
        self.driver = webdriver.Remote(self.desired_caps['remote'], desired_caps)
        self.driver.implicitly_wait(30)
        return self.driver

    def driver(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': self.desired_caps['platformVersion'],
                        'deviceName': self.desired_caps['deviceName'],
                        'appPackage': self.desired_caps['appPackage'],
                        'noReset' : 'True',  # 去掉，每次启动app都会清除数据
                        'automationName': self.desired_caps['automationName'],
                        'appActivity': self.desired_caps['appActivity'],
                        'uuid':self.desired_caps['deviceName'],
                        }
        self.driver = webdriver.Remote(self.desired_caps['remote'], desired_caps)
        self.driver.implicitly_wait(30)
        return self.driver

    def driverOld(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '5.1.1',
                        'deviceName': 'ZTE B2015',
                        'appPackage': 'com.gwchina.lssw.parent',
                        'automationName': 'Uiautomator2',
                        'noReset': 'True',  # 去掉，每次启动app都会清除数据
                        'appActivity': 'com.gwchina.tylw.parent.StartEntryActivity'
                        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)
        return self.driver

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
    print(desired_caps)
