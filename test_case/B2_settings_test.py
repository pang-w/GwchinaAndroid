# -*- coding: utf-8 -*-
from PO.po_page import B2_settings_page
import unittest
from public import GetPhoneInfo,Common,CreatePng,Log,GetSQLData,ScreenAssert
from time import sleep

log = Log.Logger(logger='SettingTest').getLog()

class SettingTest(unittest.TestCase):
    '''《通知设置和其他设置，SQL数据库对比数据》'''

    @classmethod
    def setUpClass(cls):
        log.critical("--------------------登录页面注册功能测试开始--------------------")

    def setUp(self):
        self.driver = GetPhoneInfo.Appium().driver()
        self.page = B2_settings_page.SettingPage(self.driver)
        self.base = Common.Action(self.driver)
        self.png = CreatePng.CreatePNG(self.driver)

    @ScreenAssert.decorator
    def test_setting_001_notifications(self):
        '''验证通知设置页面默认显示，截图对比'''
        self.page.click_setting()
        self.page.click_notifications()
        self.png.CreateCustomSizeNowPNG('test_setting_001_notifications',0,72,1080,1776)
        self.assertEqual(self.base.gerLocOld('test_setting_001_notifications'),self.base.getLocNow('test_setting_001_notifications'))

    @ScreenAssert.decorator
    def test_setting_002_notifications(self):
        '''验证通知设置开启和关闭系统消息功能，SQL对比'''
        self.page.click_setting()
        self.page.click_notifications()
        self.page.click_sys_switch()
        sleep(3)
        status_code = GetSQLData.get_user_set_update('system_message_notify')
        self.assertEqual(status_code,[{'param_value': '0'}])
        sleep(2)
        self.page.click_sys_switch()
        sleep(3)
        status_code = GetSQLData.get_user_set_update('system_message_notify')
        self.assertEqual(status_code,[{'param_value': '1'}])

    @ScreenAssert.decorator
    def test_setting_003_notifications(self):
        '''验证通知设置开启和关闭系统消息功能，SQL对比'''
        self.page.click_setting()
        self.page.click_notifications()
        self.page.click_sms_switch()
        sleep(3)
        status_code_0 = GetSQLData.get_user_set_update('dynamic_message_notify')
        self.assertEqual(status_code_0,[{'param_value': '0'}])
        sleep(2)
        self.page.click_sms_switch()
        sleep(3)
        status_code_1 = GetSQLData.get_user_set_update('dynamic_message_notify')
        self.assertEqual(status_code_1,[{'param_value': '1'}])

    @ScreenAssert.decorator
    def test_setting_004_toher(self):
        '''验证其他设置页面默认显示，截图对比'''
        self.page.click_setting()
        self.page.click_other()
        self.png.CreateCustomSizeNowPNG('test_setting_004_toher',0,72,1080,1776)
        self.assertEqual(self.base.gerLocOld('test_setting_004_toher'),self.base.getLocNow('test_setting_004_toher'))

    @ScreenAssert.decorator
    def test_setting_005_toher(self):
        '''验证其他设置开启远程截屏时弹窗提示，截图对比，默认不勾选下次不在提醒'''
        self.page.click_setting()
        self.page.click_other()
        self.base.click_point(980, 356)
        self.png.CreateCustomSizeNowPNG('test_setting_005_toher',81,612,999,1239)
        self.assertEqual(self.base.gerLocOld('test_setting_005_toher'),self.base.getLocNow('test_setting_005_toher'))

    @ScreenAssert.decorator
    def test_setting_006_toher(self):
        '''验证其他设置开启远程截屏时弹窗提示，不勾选下次不在提醒，在开启远程截屏时提示'''
        self.page.click_setting()
        self.page.click_other()
        self.base.click_point(980, 356)
        self.page.click_i_kown()
        self.base.is_display('id',self.page.back_btn[1])
        self.base.click_point(980, 356)
        self.base.is_display('id',self.page.back_btn[1])
        self.base.click_point(980, 356)
        self.png.CreateCustomSizeNowPNG('test_setting_006_toher',81,612,999,1239)
        self.assertEqual(self.base.gerLocOld('test_setting_005_toher'),self.base.getLocNow('test_setting_006_toher'))

    @ScreenAssert.decorator
    def test_setting_007_toher(self):
        '''验证其他设置开启远程截屏时弹窗提示，不勾选下次不在提醒，在开启远程截屏时提示'''
        self.page.click_setting()
        self.page.click_other()
        self.base.click_point(980, 356)
        self.page.click_never_remind()
        self.page.click_i_kown()
        self.base.is_display('id', self.page.back_btn[1])
        self.base.click_point(980, 356)
        self.base.is_display('id', self.page.back_btn[1])
        self.base.click_point(980, 356)
        self.base.is_display('id', self.page.back_btn[1])
        self.assertIsNotNone(self.base.get_assert('id',self.page.back_btn[1]))

    @ScreenAssert.decorator
    def test_setting_008_toher(self):
        '''验证其他设置开启、关闭远程截屏功能，SQL对比'''
        self.page.click_setting()
        self.page.click_other()
        self.base.click_point(980, 356)
        self.base.is_display('id',self.page.back_btn[1])
        status_code_1 = GetSQLData.get_user_set_update('screenshotctrl')
        self.assertEqual(status_code_1,[{'param_value': '0'}])
        self.base.click_point(980, 356)
        self.base.is_display('id',self.page.back_btn[1])
        status_code_1 = GetSQLData.get_user_set_update('screenshotctrl')
        self.assertEqual(status_code_1,[{'param_value': '1'}])

    @ScreenAssert.decorator
    def test_setting_009_toher(self):
        '''验证其他设置开启、关闭锁屏静音功能，SQL对比'''
        self.page.click_setting()
        self.page.click_other()
        self.base.click_point(974, 525)
        self.base.is_display('id',self.page.back_btn[1])
        status_code_1 = GetSQLData.get_user_set_update('lock_mute')
        self.assertEqual(status_code_1,[{'param_value': '1'}])
        self.base.click_point(974, 525)
        self.base.is_display('id',self.page.back_btn[1])
        status_code_1 = GetSQLData.get_user_set_update('lock_mute')
        self.assertEqual(status_code_1,[{'param_value': '0'}])

    @ScreenAssert.decorator
    def test_setting_010_toher(self):
        '''验证进入通知设置返回功能'''
        self.page.click_setting()
        self.page.click_notifications()
        self.page.click_back()
        self.assertIsNotNone(self.base.get_assert('xpath',self.page.other_loc[1]))

    @ScreenAssert.decorator
    def test_setting_011_toher(self):
        '''验证进入其他设置返回功能'''
        self.page.click_setting()
        self.page.click_other()
        self.page.click_back()
        self.assertIsNotNone(self.base.get_assert('xpath',self.page.notifications_loc[1]))

    def tearDown(self):
        sleep(1)
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        log.critical("--------------------登录功能测试结束--------------------")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SettingTest)
    unittest.TextTestRunner(verbosity=2).run(suite)