__author__ = 'Never deter till tomorrow that which you can do today. _20180131'
# -*- coding: utf-8 -*-

'''
获取apk包名以及版本，需要使用aapt工具，aapt.exe工具已放到百度云盘，下载至本地可放在‘.\Java\\android-sdk-windows\\tools’目录下，已加入系统path
floor() 函数返回数字的下舍整数。
subprocess通过子进程来执行外部指令，并通过input/output/error管道，获取子进程的执行的返回信息。
split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
decode() 方法以 encoding 指定的编码格式解码字符串。默认编码为字符串编码。

...Administrator>aapt dump badging E:\MyGetAppiumLearn\ApkData\GreenBox_Parent_v6.0.0_Nightly_Cs_1801290007.apk
package: name='com.gwchina.lssw.parent' versionCode='6000' versionName='6.0.0'
sdkVersion:'16'
targetSdkVersion:'22'
'''
from math import floor
import subprocess
import os

AppPath1 = os.path.dirname(os.path.abspath('.')) + '\\ApkData\\GreenBox_Parent_v6.0.0_Nightly_Cs_1801290007.apk'

class ApkInfo(object):

    def __init__(self,apkPath):
        self.apkPath = apkPath

    # 得到app的文件大小,floor() 函数返回数字的下舍整数。
    def getApkSize(self):
        size = floor(os.path.getsize(self.apkPath)/(1024*1000))
        return str(size) + "M"

    #得到包名 com.gwchina.lssw.parent
    def getApkName(self):
        cmd = "aapt dump badging " + self.apkPath
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output.split()[1].decode()[5:]
        return result

    #得到版本 6.0.0
    def getApkVersion(self):
        cmd = "aapt dump badging " + self.apkPath
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output.split()[3].decode()[12:]
        return result

    #得到启动类 com.gwchina.tylw.parent.StartEntryActivity
    def getApkActivity(self):
        cmd = "aapt dump badging " + self.apkPath
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output.split()[160].decode()[5:]
        return result

    def desired_caps(self):
        from selenium import webdriver
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '5.1.1',
                        'deviceName': 'msm8916_64',
                        'appPackage': ApkInfo(apkPath=AppPath1).getApkName(),
                        'noReset' : 'True',  # 去掉，每次启动app都会清除数据
                        'automationName': 'Uiautomator2',
                        'appActivity': ApkInfo(apkPath=AppPath1).getApkActivity()
                        }
        self.driver = webdriver.Remote('http://localhost:4721/wd/hub', desired_caps)

        return self.driver

if __name__ == '__main__':
    AppPath1 = os.path.dirname(os.path.abspath('.')) + '\\ApkData\\GreenBox_Parent_v6.0.0_Nightly_Cs_1801290007.apk'
    # AppPath1 = os.path.dirname(os.path.abspath('.')) + '\\ApkData\\t.apk'
    print(ApkInfo(apkPath=AppPath1).getApkSize())
    print(ApkInfo(apkPath=AppPath1).getApkName())
    print(ApkInfo(apkPath=AppPath1).getApkVersion())
    print(ApkInfo(apkPath=AppPath1).getApkActivity())

    # time = 0
    # while time <= 1000:
    #     print('AppPath1 %s ' % ApkInfo(apkPath=AppPath1).get_apk_activity())
    #     print('AppPath2 %s ' % ApkInfo(apkPath=AppPath2).get_apk_activity())
    #     print('AppPath3 %s ' % ApkInfo(apkPath=AppPath3).get_apk_activity())
    #     time += 1

    # print(ApkInfo(apkPath=AppPath).get_apk_version())