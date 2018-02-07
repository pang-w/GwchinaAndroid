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

log.info('删除page_path图片,删除loc_now_path图片')
DefNowPng.del_files(page_path)
DefNowPng.del_files(loc_now_path)

def Creatsuite():
    testUnit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(casePath, pattern='*_test.py', top_level_dir=None)
    for test_suite in discover:
        for caseName in test_suite:
            testUnit.addTest(caseName)
        # print(testUnit)
    return testUnit

def reportHtml():
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

def sendEmail():
    html_path = os.path.dirname(os.path.abspath('.')) + '\\report\\report_html\\' + day
    log_path = os.path.dirname(os.path.abspath('.')) + '\\log\\' + day

    HtmlPath = SendEmail.FindNewHtml(html_path)
    LogPath = SendEmail.FindNewLog(log_path)
    SendEmail.SendEmail(HtmlPath,LogPath)

if __name__ == '__main__':
    node = phoneGetConfigInfo.ReadConfig().readAppiumData()['config']
    try:
        sleep(5)
        '''stopAppiumServer'''
        AppiumServer.appiumServerNew().stopServer()
    finally:
        '''startAppiumServer'''
        sleep(5)
        AppiumServer.appiumServerNew().startServer(node)
        sleep(20)

    Creatsuite()
    reportHtml()
    sendEmail()

    sleep(5)
    '''stopAppiumServer'''
    AppiumServer.appiumServerNew().stopServer()