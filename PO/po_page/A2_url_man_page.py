from time import sleep
from public import Common,Log
from PO.po_btn import A2_url_man_btn
from selenium.webdriver.common.by import By

log = Log.Logger(logger='url_page').getLog()

class url_page(Common.Action):

    url_btn_loc = (By.XPATH,'//android.widget.TextView[@text="网址管理"]') #网址管理按钮
    back_btn_loc = (By.ID, 'com.gwchina.lssw.parent:id/iv_back')#网址管理返回按钮
    save_btn_loc = (By.ID, 'com.gwchina.lssw.parent:id/btn_action')#保存/删除按钮（右上角）
    def click_url_btn(self):
        self.find_element(*self.url_btn_loc).click()
    def click_back_btn(self):
        self.find_element(*self.back_btn_loc).click()
    def click_save_or_delete_btn(self):
        self.find_element(*self.save_btn_loc).click()

    rank_btn_loc = (By.XPATH, '//android.widget.TextView[@text="管理等级"]')#管理等级按钮
    expand_btn_loc = (By.ID, 'com.gwchina.lssw.parent:id/iv_expand')#收起/更多设置按钮（默认展开对应收起按钮）
    level_btn_loc = (By.ID,'com.gwchina.lssw.parent:id/tv_hint')#XX 模式下，不允许孩子上网的类型
    level_low_btn_loc = (By.ID, 'com.gwchina.lssw.parent:id/tv_level_low')#轻松模式按钮
    level_middle_btn_loc = (By.ID, 'com.gwchina.lssw.parent:id/tv_level_middle')#标准模式按钮
    level_high_btn_loc = (By.ID, 'com.gwchina.lssw.parent:id/tv_level_high')#严格模式按钮
    def click_rank_btn(self):
        self.find_element(*self.rank_btn_loc).click()
    def click_expand_btn(self):
        self.find_element(*self.expand_btn_loc).click()
    def click_level_btn(self):
        self.find_element(*self.level_btn_loc).click()
    def click_level_low_btn(self):
        self.find_element(*self.level_low_btn_loc).click()
    def click_level_middle_btn(self):
        self.find_element(*self.level_middle_btn_loc).click()
    def click_level_high_btn(self):
        self.find_element(*self.level_high_btn_loc).click()

    popup_nick_loc = (By.ID, 'com.gwchina.lssw.parent:id/ed_nick')#添加黑/白/关键字弹窗输入文本框
    popup_negative_loc = (By.ID, 'com.gwchina.lssw.parent:id/btn_negative')#添加黑/白/关键字弹窗取消按钮
    popup_positive_loc = (By.ID, 'com.gwchina.lssw.parent:id/btn_positive')#添加黑/白/关键字弹窗确定按钮
    one_cb_loc = (By.ID, 'com.gwchina.lssw.parent:id/cb')#选择单个删除勾选按钮
    all_cb_loc = (By.ID, 'com.gwchina.lssw.parent:id/cb_selectall')#全选删除按钮
    delete_loc = (By.ID, 'com.gwchina.lssw.parent:id/btn_delete')#底部删除按钮（右下角）
    url_value_loc = (By.ID, 'com.gwchina.lssw.parent:id/tv_url')#已添加的网址url按钮
    url_popup_nick_name = (By.ID, 'com.gwchina.lssw.parent:id/ed_nick_name')#编辑网址名称文本框按钮
    url_popup_nick_url = (By.ID,'com.gwchina.lssw.parent:id/ed_nick')#编辑网址名称文本框按钮
    black_btn_loc = (By.XPATH, '//android.widget.TextView[@text="黑名单"]')#黑名单按钮
    add_black_and_white_btn_loc = (By.ID, 'com.gwchina.lssw.parent:id/btn_add')#添加黑名单按钮
    white_btn_loc = (By.XPATH, '//android.widget.TextView[@text="白名单"]')#白名单按钮
    find_no_child_btn = (By.ID, 'com.gwchina.lssw.parent:id/message')#您尚未绑定孩子设备，暂时无法操作
    homepage_child_head_btn = (By.ID, 'com.gwchina.lssw.parent:id/tv_child_nick')#主页上孩子头像按钮（如果存在=刷新出设备）

    def input_popup_nick(self,value):
        self.find_element(*self.popup_nick_loc).send_keys(value)
    def input_popup_nick_clear(self):
        self.find_element(*self.popup_nick_loc).clear()
    def click_popup_negative_btn(self):
        self.find_element(*self.popup_negative_loc).click()
    def click_popup_positive_btn(self):
        self.find_element(*self.popup_positive_loc).click()
    def click_one_cb(self):
        self.find_element(*self.one_cb_loc).click()
    def click_all_cb(self):
        self.find_element(*self.all_cb_loc).click()
    def click_delete_btn(self):
        self.find_element(*self.delete_loc).click()
    def click_url_value(self):
        self.find_element(*self.url_value_loc).click()
    def input_popup_nick_name(self,value):
        self.find_element(*self.url_popup_nick_name).clear()
        self.find_element(*self.url_popup_nick_name).send_keys(value)
    def input_popup_nick_url(self, value):
        self.find_element(*self.url_popup_nick_url).clear()
        self.find_element(*self.url_popup_nick_url).send_keys(value)
    def click_black_btn(self):
        self.find_element(*self.black_btn_loc).click()
    def click_white_btn(self):
        self.find_element(*self.white_btn_loc).click()
    def click_add_black_btn(self):
        self.find_element(*self.add_black_and_white_btn_loc).click()
    def click_add_white_btn(self):
        self.find_element(*self.add_black_and_white_btn_loc).click()
    def input_nick_value(self,value):
        self.click_add_black_btn()
        self.input_popup_nick(value)
        self.click_popup_positive_btn()

    def go_url_homepage(self):
        sleep(8)
        self.is_display(self.homepage_child_head_btn[1])
        self.click_url_btn()
        # loc = self.is_display_loc(self.rank_btn_loc)
        # time = 1
        # while loc == False and time <= 5:
        #     log.info('A2_url_man_test（go_url_homepage）未刷新出孩子设备，第 %s 次重试' % time)
        #     print('A2_url_man_test（go_url_homepage）未刷新出孩子设备，第 %s 次重试' % time)
        #     sleep(2)
        #     self.click_popup_negative_btn()
        #     sleep(5)
        #     self.click_url_btn()
        #     sleep(2)
        #     time += 1
        #     loc = self.is_display_loc(self.rank_btn_loc)
        #     if time > 5:
        #         log.info('A2_url_man_test（go_url_homepage）尝试刷新5次孩子设备，未刷新出孩子设备，多数为网络原因')
        #         print('A2_url_man_test（go_url_homepage）尝试刷新5次孩子设备，未刷新出孩子设备，多数为网络原因')
        #         break

    def go_black_list(self):
        self.go_url_homepage()
        self.click_black_btn()
    def go_white_list(self):
        self.go_url_homepage()
        self.click_white_btn()
    def add_black_url(self,url):
        self.go_url_homepage()
        self.click_black_btn()
        self.click_add_black_btn()
        self.input_popup_nick(url)
        self.click_popup_positive_btn()
    def add_white_url(self,url):
        self.go_url_homepage()
        self.click_white_btn()
        self.click_add_black_btn()
        self.input_popup_nick(url)
        self.click_popup_positive_btn()
    def del_url(self):
        self.click_save_or_delete_btn()
        self.click_all_cb()
        self.click_delete_btn()
        self.click_popup_positive_btn()
        self.is_display(self.save_btn_loc[1])

    #关键字
    key_btn = (By.XPATH,'//android.widget.TextView[@text="关键字"]')
    key_switch_btn = (By.ID, 'com.gwchina.lssw.parent:id/btn_switch')
    add_key_btn = (By.ID, 'com.gwchina.lssw.parent:id/btn_add')
    def click_key(self):
        self.find_element(*self.key_btn).click()
    def click_key_switch(self):
        self.find_element(*self.key_switch_btn).click()
    def click_add_key(self):
        self.find_element(*self.add_key_btn).click()
    def go_key(self):
        self.go_url_homepage()
        self.click_key()