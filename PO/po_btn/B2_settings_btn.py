# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

config = {
    'setting_loc': (By.ID, 'com.gwchina.lssw.parent:id/rb_settings'),
    'back_btn': (By.ID, 'com.gwchina.lssw.parent:id/iv_back'),
    #以下notifications_settings
    'notifications_loc': (By.XPATH, '//android.widget.TextView[@text="通知设置"]'), #notifications_
    'sys_switch_btn':(By.ID,'com.gwchina.lssw.parent:id/btn_sys_switch'),  #系统消息切换按钮
    'sms_switch_btn': (By.ID, 'com.gwchina.lssw.parent:id/btn_account_switch'), #动态消息切换按钮
    # other_settings
    'other_loc': (By.XPATH, '//android.widget.TextView[@text="其他设置"]'),  # notifications
    'i_kown_btn':(By.ID,'com.gwchina.lssw.parent:id/tv_confirm'),
    'never_remind_btn':(By.ID,'com.gwchina.lssw.parent:id/cb_never_remind'), #下次不在提醒按钮
}
