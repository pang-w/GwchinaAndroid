from PO.po_btn import A3_time_man_btn
from public import Common,Log
from time import sleep
import datetime
from selenium.webdriver.common.by import By

log = Log.Logger(logger='time_page').getLog()

class time_page(Common.Action):

    time_btn_loc = (By.XPATH, '//android.widget.TextView[@text="时间管理"]')
    Guide_home_page_btn = (By.ID,'com.gwchina.lssw.parent:id/iv_time_guide')
    Guide_confirm_page_btn = (By.ID, 'com.gwchina.lssw.parent:id/tv_confirm')
    more_btn = (By.ID,'com.gwchina.lssw.parent:id/tv_more')
    save_btn = (By.ID,'com.gwchina.lssw.parent:id/btn_action')
    save_negative_btn = (By.ID, 'com.gwchina.lssw.parent:id/btn_negative')
    save_positive_btn = (By.ID, 'com.gwchina.lssw.parent:id/btn_positive')
    back_btn = (By.ID,'com.gwchina.lssw.parent:id/iv_back')

    def click_time_btn(self):
        sleep(5)
        self.find_element(*self.time_btn_loc).click()
    def click_Guide_confirm(self):
        self.find_element(*self.Guide_confirm_page_btn).click()
    def click_more(self):
        self.find_element(*self.more_btn).click()
    def click_save(self):
        self.find_element(*self.save_btn).click()
    def click_save_negative(self):
        self.find_element(*self.save_negative_btn).click()
    def click_save_positive(self):
        self.find_element(*self.save_positive_btn).click()
        self.is_display_loc(self.save_btn)
    def click_back(self):
        self.find_element(*self.back_btn).click()

    time_1_btn = (By.XPATH, '//android.widget.TextView[@text="一"]')
    time_2_btn = (By.XPATH, '//android.widget.TextView[@text="二"]')
    time_3_btn = (By.XPATH, '//android.widget.TextView[@text="三"]')
    time_4_btn = (By.XPATH, '//android.widget.TextView[@text="四"]')
    time_5_btn = (By.XPATH, '//android.widget.TextView[@text="五"]')
    time_6_btn = (By.XPATH, '//android.widget.TextView[@text="六"]')
    time_7_btn = (By.XPATH, '//android.widget.TextView[@text="日"]')

    def click_time_1(self):
        self.find_element(*self.time_1_btn).click()
    def click_time_2(self):
        self.find_element(*self.time_2_btn).click()
    def click_time_3(self):
        self.find_element(*self.time_3_btn).click()
    def click_time_4(self):
        self.find_element(*self.time_4_btn).click()
    def click_time_5(self):
        self.find_element(*self.time_5_btn).click()
    def click_time_6(self):
        self.find_element(*self.time_6_btn).click()
    def click_time_7(self):
        self.find_element(*self.time_7_btn).click()

    homepage_child_head_btn = (By.ID, 'com.gwchina.lssw.parent:id/tv_child_nick')#主页上孩子头像按钮（如果存在=刷新出设备）

    def go_time_homepage(self):
        self.is_display_loc(self.homepage_child_head_btn)
        self.click_time_btn()
        # loc = self.is_display_loc(self.save_btn)
        # time = 1
        # while loc == False and time <= 5:
        #     log.info('A3_time_man_test（go_time_homepage）未刷新出孩子设备，第 %s 次重试' % time)
        #     print('A3_time_man_test（go_time_homepage）未刷新出孩子设备，第 %s 次重试' % time)
        #     sleep(2)
        #     self.driver.find_element_by_id('com.gwchina.lssw.parent:id/btn_negative').click()
        #     sleep(5)
        #     self.click_time_btn()
        #     sleep(2)
        #     time += 1
        #     loc = self.is_display_loc(self.save_btn)
        #     if time > 5 :
        #         log.info('A3_time_man_test（go_time_homepage）尝试刷新5次孩子设备，未刷新出孩子设备，多数为网络原因')
        #         print('A3_time_man_test（go_time_homepage）尝试刷新5次孩子设备，未刷新出孩子设备，多数为网络原因')
        #         break

    # @classmethod
    def get_weekday(self):
        weekday = datetime.datetime.now().weekday()
        if weekday == 0:
            weekday_text = ('周一可用时段')
            return weekday_text
        elif weekday == 1:
            weekday_text = ('周二可用时段')
            return weekday_text
        elif weekday == 2:
            weekday_text = ('周三可用时段')
            return weekday_text
        elif weekday == 3:
            weekday_text = ('周四可用时段')
            return weekday_text
        elif weekday == 4:
            weekday_text = ('周五可用时段')
            return weekday_text
        elif weekday == 5:
            weekday_text = ('周六可用时段')
            return weekday_text
        elif weekday == 6:
            weekday_text = ('周日可用时段')
            return weekday_text

if __name__ == '__main__':
    a = time_page(Common.Action).get_weekday()
    print(a)