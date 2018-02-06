# -*- coding: utf-8 -*-
import unittest
from public import Common,GetPhoneInfo,GetSQLData,CreatePng,ScreenAssert
from PO.po_page import A1_homepage_page

class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.driver = GetPhoneInfo.AppiumTest().get_driver()
        self.page = A1_homepage_page.HomePage(self.driver)
        self.base = Common.Action(self.driver)
        self.png = CreatePng.CreatePNG(self.driver)

    @ScreenAssert.decorator
    def test_home_A001(self):
        '''主页面截图对比顶部头像以及默认锁屏状态，截图对比'''
        self.base.is_display('id',self.page.device_btn[1])
        self.png.CreateCustomSizeNowPNG('test_home_A001',0,75,1078,1156)
        self.assertEqual(self.base.gerLocOld('test_home_A001'),self.base.getLocNow('test_home_A001'))

    @ScreenAssert.decorator
    def test_home_A002(self):
        '''主页面点击头像跳转设备详情页面，返回到主页面'''
        self.page.click_header()
        try:
            self.base.is_display('id',self.page.title_text[1])
            self.assertEqual(self.page.get_title(),'设备详情')
        finally:
            self.page.click_all_back()
            self.assertIsNotNone(self.base.get_assert('id',self.page.header_btn[1]))

    @ScreenAssert.decorator
    def test_home_A003(self):
        '''主页面点击孩子设备名称跳转至消息页面，点击设置跳转至设备详情页面，验证标题'''
        self.page.click_device()
        try:
            self.assertEqual(self.page.get_title(), 'ZTE B2015')
        finally:
            try:
                self.page.click_setting()
                self.assertEqual(self.page.get_title(), '设备详情')
            finally:
                try:
                    self.page.click_all_back()
                    self.assertEqual(self.page.get_title(), 'ZTE B2015')
                finally:
                    self.page.click_all_back()
                    self.assertIsNotNone(self.base.get_assert('id', self.page.header_btn[1]))

    @ScreenAssert.decorator
    def test_home_A004(self):
        '''主页面扫码绑定页面，验证标题，验证返回功能'''
        self.page.click_bind()
        try:
            self.assertEqual(self.page.get_title(), '扫码绑定设备')
        finally:
            self.page.click_all_back()
            self.assertIsNotNone(self.base.get_assert('id', self.page.header_btn[1]))

    @ScreenAssert.decorator
    def test_home_A005(self):
        '''点击锁屏、解屏按钮，sql对比'''
        try:
            self.page.click_lock_btn()
            self.base.is_display('id',self.page.device_btn[1])
            self.assertEqual(GetSQLData.sql_locked(), 1)
        finally:
            self.page.click_lock_btn()
            self.base.is_display('id',self.page.device_btn[1])
            self.assertEqual(GetSQLData.sql_locked(), 0)

    @ScreenAssert.decorator
    def test_home_A006(self):
        '''点击锁屏后，text验证设备已锁屏文本'''
        try:
            self.page.click_lock_btn()
            self.base.is_display('id',self.page.device_btn[1])
            self.assertEqual(self.page.get_lock_stute_text(),'设备已锁屏')
        finally:
            self.page.click_lock_btn()
            self.base.is_display('id',self.page.device_btn[1])
            self.assertEqual(self.page.get_lock_stute_text(),'设备未锁屏')

    @ScreenAssert.decorator
    def test_home_A007(self):
        '''点击锁屏后，toast验证锁屏成功'''
        self.page.click_lock_btn()
        self.base.find_toast('操作成功',self.driver)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
