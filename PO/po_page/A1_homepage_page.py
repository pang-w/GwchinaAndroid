# -*- coding: utf-8 -*-
from PO.po_btn import A1_homepage_btn
from selenium.webdriver.common.by import By
from public import Common

class HomePage(Common.Action):
    all_back_btn = (By.ID,'com.gwchina.lssw.parent:id/iv_back')#头像按钮
    title_text = (By.ID,'com.gwchina.lssw.parent:id/tv_title')#头像按钮
    def click_all_back(self):
        self.find_element(*self.all_back_btn).click()
    def get_title(self):
        return self.find_element(*self.title_text).text
    header_btn = (By.ID,'com.gwchina.lssw.parent:id/header_icon')#头像按钮
    device_btn = (By.ID,'com.gwchina.lssw.parent:id/tv_child_nick')#设备按钮
    setting_btn = (By.ID,'com.gwchina.lssw.parent:id/btn_action2')#跳转聊天页面左上角的设置按钮
    bind_btn = (By.ID, 'com.gwchina.lssw.parent:id/icon') # 扫码绑定按钮
    lock_stute_text = (By.ID, 'com.gwchina.lssw.parent:id/tv_lock_stute_text')# 设备未锁屏/设备已锁屏
    lock_btn = (By.ID, 'com.gwchina.lssw.parent:id/lock_btn')# 锁屏、解屏按钮
    def click_header(self):
        self.is_display(self.device_btn[1])
        self.find_element(*self.header_btn).click()
    def click_device(self):
        self.is_display(self.device_btn[1])
        self.find_element(*self.device_btn).click()
    def click_setting(self):
        self.find_element(*self.setting_btn).click()
    def click_bind(self):
        self.is_display(self.device_btn[1])
        self.find_element(*self.bind_btn).click()
    def get_lock_stute_text(self):
        return self.find_element(*self.lock_stute_text).text
    def click_lock_btn(self):
        self.is_display(self.device_btn[1])
        self.find_element(*self.lock_btn).click()


    url_man_btn = (By.XPATH, '//android.widget.TextView[@text="网址管理"]')#网址管理
    soft_man_btn = (By.XPATH, '//android.widget.TextView[@text="软件管理"]')#软件管理
    time_man_btn = (By.XPATH, '//android.widget.TextView[@text="时间管理"]')#时间管理
    child_location_btn = (By.XPATH, '//android.widget.TextView[@text="孩子位置"]')#孩子位置
    sport_record_btn = (By.XPATH, '//android.widget.TextView[@text="运动轨迹"]')#运动轨迹
    security_area_btn = (By.XPATH, '//android.widget.TextView[@text="安全区域"]')#安全区域
    family_number_btn = (By.XPATH, '//android.widget.TextView[@text="亲情号码"]')#亲情号码
    xgl_btn = (By.XPATH, '//android.widget.TextView[@text="格雷专区"]')#格雷专区
    eye_span_btn = (By.XPATH, '//android.widget.TextView[@text="眼距提醒"]')#眼距提醒
    time_manager_btn = (By.XPATH, '//android.widget.TextView[@text="日程提醒"]')#日程提醒
    screen_shot_btn = (By.XPATH, '//android.widget.TextView[@text="远程截屏"]')#远程截屏
    def click_url_man(self):
        self.is_display(self.device_btn[1])
        self.find_element(*self.url_man_btn).click()
    def click_soft_man(self):
        self.is_display(self.device_btn[1])
        self.find_element(*self.soft_man_btn).click()
    def click_time_man(self):
        self.is_display(self.device_btn[1])
        self.find_element(*self.time_man_btn).click()
    def click_child_location(self):
        self.is_display(self.device_btn[1])
        self.find_element(*self.child_location_btn).click()
    def click_sport_record(self):
        self.is_display(self.device_btn[1])
        self.find_element(*self.sport_record_btn).click()
    def click_security_area(self):
        self.is_display(self.device_btn[1])
        self.find_element(*self.security_area_btn).click()
    def click_family_number(self):
        self.is_display(self.device_btn[1])
        self.find_element(*self.family_number_btn).click()
    def click_xgl(self):
        self.is_display(self.device_btn[1])
        self.find_element(*self.xgl_btn).click()
    def click_eye_span(self):
        self.is_display(self.device_btn[1])
        self.find_element(*self.eye_span_btn).click()
    def click_time_manager(self):
        self.is_display(self.device_btn[1])
        self.find_element(*self.time_manager_btn).click()
    def click_screen_shot(self):
        self.is_display(self.device_btn[1])
        self.find_element(*self.screen_shot_btn).click()

