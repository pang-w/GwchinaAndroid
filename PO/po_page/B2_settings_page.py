# -*- coding: utf-8 -*-
from PO.po_btn import B2_settings_btn
from public import Common
from time import sleep

class SettingPage(Common.Action):

    setting_loc = B2_settings_btn.config['setting_loc']
    back_btn = B2_settings_btn.config['back_btn']
    notifications_loc = B2_settings_btn.config['notifications_loc']
    sys_switch_btn = B2_settings_btn.config['sys_switch_btn']
    sms_switch_btn = B2_settings_btn.config['sms_switch_btn']

    other_loc = B2_settings_btn.config['other_loc']
    i_kown_btn = B2_settings_btn.config['i_kown_btn']
    never_remind_btn = B2_settings_btn.config['never_remind_btn']

    def click_setting(self):
        sleep(5)
        self.find_element(*self.setting_loc).click()
    def click_back(self):
        self.find_element(*self.back_btn).click()
    def click_notifications(self):
        self.find_element(*self.notifications_loc).click()

    def click_sys_switch(self):
        self.find_element(*self.sys_switch_btn).click()

    def click_sms_switch(self):
        self.find_element(*self.sms_switch_btn).click()


    def click_other(self):
        self.find_element(*self.other_loc).click()

    def click_i_kown(self):
        self.find_element(*self.i_kown_btn).click()

    def click_never_remind(self):
        self.find_element(*self.never_remind_btn).click()