from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from public import Log,SaveCreen
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PIL import Image
import os

absPath = os.path.dirname(os.path.abspath('.'))
log = Log.Logger(logger='Common').getLog()

class Action():

    def __init__(self,driver):
        self.driver = driver

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver, 30, 0.5).until(EC.visibility_of_element_located(loc))
            try:
                WebDriverWait(self.driver,10,0.5,).until(lambda driver: driver.find_element(*loc).is_displayed())
                return self.driver.find_element(*loc)
            except:
                SaveCreen.ScreenShot(self.driver).saveScreen()
                log.error("‘find_element(*loc).is_displayed()’ The page was not found ‘%s’ element,Save the screen shot as the ‘.\\report\\report_html’ folder " %loc[1])
        except:
            SaveCreen.ScreenShot(self.driver).saveScreen()
            log.error("‘EC.visibility_of_element_located(loc)’ The page was not found ‘%s’ element,Save the screen shot as the ‘.\\report\\report_html’ folder " % loc[1])

    # 一直等待某元素可见
    def is_display(self,mode,locator):
        try:
            if mode == 'id':
                WebDriverWait(self.driver,30,0.5).until(EC.visibility_of_element_located((By.ID, locator)))
                # print('is_display已找到 %s 元素' % locator)
                return True
            elif mode == 'xpath':
                WebDriverWait(self.driver,30,0.5).until(EC.visibility_of_element_located((By.XPATH, locator)))
                # print('is_display已找到 %s 元素' % locator)
                return True

        except:
            log.error("‘is_display’ Failed to find ‘%s’ elements" % locator)
            # print('is_display未找到 %s 元素' % locator)
            return False

    def is_display_loc(self,locator):
        try:
            WebDriverWait(self.driver,30,0.5).until(EC.visibility_of_element_located(locator))
            # print('is_display_loc已找到元素')
            return True
        except:
            # My_log.info("is_display_loc未能找到 %s 元素" % locator)  加上这个出错
            log.error("‘is_display_loc’ Failed to find ‘%s’ elements" % locator)
            return False

    #断言，先查找\定位按钮后在断言，避免断言出错
    def get_assert(self,mode,value):
        self.is_display(mode,value)
        return self.driver.find_element(mode,value)

    def get_assert_loc(self,loc):
        self.is_display_loc(loc)
        return self.driver.find_element(loc)

    def find_toast(self, message, driver):
        message = '//*[@text=\'{}\']'.format(message)
        element = WebDriverWait(driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, message)))
        return element

    def get_size(self):
        size = self.driver.get_window_size()
        return size

    def swipe_to_down(self,start_y,end_y):
        # 下滑屏幕
        sleep(2)
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        print(width,height)
        self.driver.swipe(width / 2, height / start_y, width / 2, height / end_y,  1000)
        sleep(2)
        '''
        height * 0.78 = 1500
        height / 10 = 190
        '''
    def swipe_screen(self,start_x,start_y,end_x,end_y,time):
        # 自定义滑动屏幕  time 单位 5000 == 5s
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        print(width,height)
        self.driver.swipe(start_x, start_y, end_x, end_y, time)
        sleep(1)
    def click_point(self,piont_x,piont_y):
        sleep(1)
        self.driver.tap([(piont_x,piont_y)],100)
        sleep(1)

    def gerLocOld(self,PNG):
        old = Image.open(absPath + '\\data\\loc_old\\%s.png' % PNG)
        return old

    def getLocNow(self,PNG):
        now = Image.open(absPath + '\\data\\loc_now\\%s.png' % PNG)
        return now

