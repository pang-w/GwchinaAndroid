import time, os

ScreenPath = os.path.dirname(os.path.abspath('.')) + '\\report\\report_png\\'

class ScreenShot(object):

    def __init__(self,driver):
        self.driver = driver

    def saveScreen(self):
        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        tdResult = ScreenPath + day
        filename = tdResult + "\\" + now + ".png"
        if not os.path.exists(tdResult):
            os.mkdir(tdResult)
        else:
            pass
        self.driver.get_screenshot_as_file(filename)

if __name__ == '__main__':
    pass