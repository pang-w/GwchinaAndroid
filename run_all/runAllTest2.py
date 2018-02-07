__author__ = 'Never deter till tomorrow that which you can do today. _20180131'
# -*- coding: utf-8 -*-

'''
自动开启AppiumServer
集成测试用例
发送测试报告邮件
自动关闭AppiumServer
'''
import unittest
import os,time
from time import sleep
from public import SendEmail
from testDAL import AppiumServer
from config import phoneGetConfigInfo
from public import HTMLTestRunner,DefNowPng,Log

log = Log.Logger(logger='runAllTest').getLog()
absPath = os.path.dirname(os.path.abspath('.'))
casePath = absPath + '\\test_case'
report = absPath + "\\report\\report_html\\"
page_path = absPath + '\\data\\page\\'
loc_now_path = absPath + '\\data\\loc_now\\'
node = phoneGetConfigInfo.ReadConfig().readAppiumData()['config']

# try:
#     sleep(5)
#     '''stopAppiumServer'''
#     AppiumServer.appiumServerNew().stopServer()
# finally:
#     '''startAppiumServer'''
#     sleep(5)
#     AppiumServer.appiumServerNew().startServer(node)
#     sleep(20)
#
# log.info('删除page_path图片,删除loc_now_path图片')
# DefNowPng.del_files(page_path)
# DefNowPng.del_files(loc_now_path)

def Creatsuite():
    testUnit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(casePath, pattern='*_test1.py', top_level_dir=None)
    for test_suite in discover:
        for caseName in test_suite:
            testUnit.addTest(caseName)
        print(testUnit)
    return testUnit

def writeHtml():
    test_case = Creatsuite()
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    tdResult = report + day
    if os.path.exists(tdResult):
        filename = tdResult + "\\" + now + "_result.html"
        fp = open(filename,'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream = fp, title ='格雷盒子Android家长端测试报告', description ='用例执行情况： ')
        runner.run(test_case)
        print('-------------------------- 测试结束 --------------------------')
        fp.close()
    else:
        os.mkdir(tdResult)
        filename = tdResult + "\\" + now + "_result.html"
        fp = open(filename,'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream = fp, title ='格雷盒子Android家长端测试报告', description ='用例执行情况： ')
        runner.run(test_case)
        print('-------------------------- 测试结束 --------------------------')
        fp.close()

if __name__ == '__main__':
    AppiumServer.appiumServerNew().startServer(node)
    sleep(20)
    Creatsuite()
    writeHtml()