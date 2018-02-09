__author__ = 'Never deter till tomorrow that which you can do today. _20180131'
# -*- coding: utf-8 -*-

import configparser,os
from config import phoneWriteConfigInfo

class ReadConfig(object):

    phoneWriteConfigInfo.writePhoneInfo().write()

    def __init__(self):
        self.configPath = os.path.dirname(os.path.abspath('.')) + '\\config\\phoneConfigDevices.ini'
        self.config = configparser.ConfigParser()
        self.config.read(self.configPath)
        self.configAppiumDict = {'devices':'','port':'','config':'','platformName':''}
        self.configDesiredCapsDict = {'platformName':'','platformVersion':'','deviceName':'','appPackage':'','automationName':'',
                                      'appActivity':'','uuid':'','remote':''}

    def readAppiumData(self):
        self.configAppiumDict['devices'] = self.config.get('appium','devices')
        self.configAppiumDict['port'] = self.config.get('appium','port')
        self.configAppiumDict['config'] = self.config.get('appium','config')
        self.configAppiumDict['platformName'] = self.config.get('appium','platformName')
        return self.configAppiumDict

    def readDesiredCapsData(self):
        self.configDesiredCapsDict['platformName'] = self.config.get('desired_caps','platformName')
        self.configDesiredCapsDict['platformVersion'] = self.config.get('desired_caps','platformVersion')
        self.configDesiredCapsDict['deviceName'] = self.config.get('desired_caps','deviceName')
        self.configDesiredCapsDict['appPackage'] = self.config.get('desired_caps','appPackage')
        self.configDesiredCapsDict['automationName'] = self.config.get('desired_caps','automationName')
        self.configDesiredCapsDict['appActivity'] = self.config.get('desired_caps','appActivity')
        self.configDesiredCapsDict['uuid'] = self.config.get('desired_caps','uuid')
        self.configDesiredCapsDict['remote'] = self.config.get('desired_caps','remote')
        return self.configDesiredCapsDict

if __name__ == '__main__':
    print(ReadConfig().readAppiumData())
    print(ReadConfig().readAppiumData()['port'])

    print(ReadConfig().readDesiredCapsData()['platformName'])
    print(ReadConfig().readDesiredCapsData()['platformVersion'])
    print(ReadConfig().readDesiredCapsData()['deviceName'])
    print(ReadConfig().readDesiredCapsData()['appPackage'])
    print(ReadConfig().readDesiredCapsData()['automationName'])
    print(ReadConfig().readDesiredCapsData()['appActivity'])
    print(ReadConfig().readDesiredCapsData()['uuid'])
    print(ReadConfig().readDesiredCapsData()['remote'])
