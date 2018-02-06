# coding: utf-8
import time,os
from functools import wraps
from public import Log

'''
断言装饰器，仅适用于在测试用例断言失败时截图保存至 \\report\\assert_png\\%s'" % day
当函数的参数不确定时，可以使用*args 和**kwargs，*args 没有key值，**kwargs有key值。
'''

logAssert = Log.Logger(logger='screenAssert').getLog()
logTestIDInfo = Log.Logger(logger='TestIDInfo').getLog()

abs_path = os.path.dirname(os.path.abspath('.'))

def decorator(func):
    @wraps(func)
    def getscreenShot(self, *args, **kwargs):
        try:
            logTestIDInfo.critical('Test case ID: %s ' % func.__name__)
            return func(self, *args, **kwargs)
        except Exception as e:
            now_time = time.strftime('%H-%M-%S', time.localtime(time.time()))
            day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            assert_path = abs_path + '\\report\\assert_png\\' + day + '\\'
            if os.path.exists(assert_path):
                png_name = os.path.join(assert_path + '%s_' % now_time + '%s.png' % func.__name__)
                self.driver.get_screenshot_as_file(png_name)
            else:
                os.mkdir(r'%s' % assert_path)
                png_name = os.path.join(assert_path + '%s_' % now_time + '%s.png' % func.__name__)
                self.driver.get_screenshot_as_file(png_name)
            logAssert.error("Test case assertion failureGet, error info ( %s )" % e)
            logAssert.error("Test case assertion failureGet, the screen shot to save to '\\report\\assert_png\\%s'" % day)
            raise e
    return getscreenShot