'''
自动开启AppiumServer
集成测试用例
发送测试报告邮件
自动关闭AppiumServer
'''
import os,time
from time import sleep
from public import SendEmail
import unittest

from public import HTMLTestRunner,DefNowPng,Log

log = Log.Logger(logger='runAllTest').getLog()
absPath = os.path.dirname(os.path.abspath('.'))

casePath = absPath + '\\test_case'
report = absPath + "\\report\\report_html\\"

page_path = absPath + '\\data\\page\\'
loc_now_path = absPath + '\\data\\loc_now\\'

def Creatsuite():
    testUnit = unittest.TestSuite()

    discover = unittest.defaultTestLoader.discover(casePath, pattern='*_test.py', top_level_dir=None)

    for test_suite in discover:
        for caseName in test_suite:
            testUnit.addTest(caseName)
        print(testUnit)
    return testUnit

'''startAppiumServer'''
startAppiumServer = absPath + '\\appiumserver\\startAppiumServer.bat'
os.system('start %s ' % startAppiumServer)
sleep(20)

log.info('删除page_path图片,删除loc_now_path图片')
DefNowPng.del_files(page_path)
DefNowPng.del_files(loc_now_path)

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

html_path = os.path.dirname(os.path.abspath('.')) + '\\report\\report_html\\' + day
log_path = os.path.dirname(os.path.abspath('.')) + '\\log\\' + day

HtmlPath = SendEmail.FindNewHtml(html_path)
LogPath = SendEmail.FindNewLog(log_path)
SendEmail.SendEmail(HtmlPath,LogPath)

sleep(5)
'''stopAppiumServer'''
stopAppiumServer = absPath + '\\appiumserver\\stopAppiumServer.bat'
os.system('start %s ' % stopAppiumServer)
