__author__ = 'Never deter till tomorrow that which you can do today. _20180131'
# -*- coding: utf-8 -*-

import os
import time
import configparser
from testDAL import adbCommon
from testDAL import phoneBase
from testDAL import apkBaseInfo
from config import configReadInfo

now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
apkPath = os.path.dirname(os.path.abspath('.')) + '\\ApkData\\GreenBox_Parent_v6.0.0_Nightly_Cs_1801290007.apk'
absPath = os.path.dirname(os.path.abspath('.'))


class writePhoneInfo(object):

    def __init__(self):

        self.devices = adbCommon.AndroidDebugBridge().attachedDevices()
        self.platformVersion = phoneBase.getPhoneInfo(self.devices)['release']
        self.appPackage = apkBaseInfo.ApkInfo(apkPath).getApkName()
        self.appActivity = apkBaseInfo.ApkInfo(apkPath).getApkActivity()
        self.config = configparser.ConfigParser()
        self.port = configReadInfo.ReadConfig().readDeviceInfo()['port']
        self.platformName = configReadInfo.ReadConfig().readDeviceInfo()['platformName']

    def write(self):
        # set a number of parameters
        self.config.add_section('time')
        self.config.set('time','now',now)

        self.config.add_section("appium")
        self.config.set("appium", "devices", self.devices)
        self.config.set("appium", "port", self.port)
        self.config.set("appium", "config", r"node C:\Users\Administrator\AppData\Local\Programs\appium-desktop\resources\app\node_modules\appium\build\lib\main.js -p %s -bp 4724 -U %s" % (self.port,self.devices))
        self.config.set("appium", "platformName", self.platformName)

        self.config.add_section("desired_caps")
        self.config.set("desired_caps", "platformName", self.platformName)
        self.config.set("desired_caps", "platformVersion", self.platformVersion)
        self.config.set("desired_caps", "deviceName", self.devices)
        self.config.set("desired_caps", "appPackage", self.appPackage)
        self.config.set("desired_caps", "automationName", "Uiautomator2")
        self.config.set("desired_caps", "appActivity", self.appActivity)
        self.config.set("desired_caps", "uuid", self.devices)
        self.config.set("desired_caps", "Remote", "http://localhost:%s/wd/hub" % self.port)

        # write to file
        self.config.write(open(absPath + '\\config\\phoneConfigDevices.ini', "w"))

if __name__ =='__main__':
    writePhoneInfo().write()
    port = int(configReadInfo.ReadConfig().readDeviceInfo()['port']) + 1
    print(port)