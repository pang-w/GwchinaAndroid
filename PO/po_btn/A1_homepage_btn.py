# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

'''
弃用
元素直接写入page内
'''

config = {
    'all_back_btn':(By.ID,'com.gwchina.lssw.parent:id/iv_back'),
    'title_text':(By.ID,'com.gwchina.lssw.parent:id/tv_title'),
    'header_btn':(By.ID,'com.gwchina.lssw.parent:id/header_icon'),#头像按钮
    'device_btn':(By.ID,'com.gwchina.lssw.parent:id/tv_child_nick'),#设备按钮
    'setting_btn':(By.ID,'com.gwchina.lssw.parent:id/btn_action2'),#跳转聊天页面左上角的设置按钮
    'bind_btn': (By.ID, 'com.gwchina.lssw.parent:id/icon'),  # 扫码绑定按钮
    'lock_stute_text': (By.ID, 'com.gwchina.lssw.parent:id/tv_lock_stute_text'),  # 设备未锁屏/设备已锁屏
    'lock_btn': (By.ID, 'com.gwchina.lssw.parent:id/lock_btn'),  # 锁屏、解屏按钮
    'url_man_btn': (By.XPATH, '//android.widget.TextView[@text="网址管理"]'),
    'soft_man_btn': (By.XPATH, '//android.widget.TextView[@text="软件管理"]'),
    'time_man_btn': (By.XPATH, '//android.widget.TextView[@text="时间管理"]'),
    'child_location_btn': (By.XPATH, '//android.widget.TextView[@text="孩子位置"]'),
    'sport_record_btn': (By.XPATH, '//android.widget.TextView[@text="运动轨迹"]'),
    'security_area_btn': (By.XPATH, '//android.widget.TextView[@text="安全区域"]'),
    'family_number_btn': (By.XPATH, '//android.widget.TextView[@text="亲情号码"]'),
    'xgl_btn': (By.XPATH, '//android.widget.TextView[@text="格雷专区"]'),
    'eye_span_btn': (By.XPATH, '//android.widget.TextView[@text="眼距提醒"]'),
    'time_manager_btn': (By.XPATH, '//android.widget.TextView[@text="日程提醒"]'),
    'screen_shot_btn': (By.XPATH, '//android.widget.TextView[@text="远程截屏"]'),
    # 'screen_shot_btn': (By.XPATH, '//android.widget.TextView[@text="远程截屏"]'),
    # 'screen_shot_btn': (By.XPATH, '//android.widget.TextView[@text="远程截屏"]'),
}