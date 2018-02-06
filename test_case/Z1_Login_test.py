import unittest
from public import Log, Common,GetPhoneInfo,CreatePng,ScreenAssert
from PO.po_page import Z1_Login_page
from time import sleep

log = Log.Logger(logger='LoginTest').getLog()

import os
from Phone import getYamlData
from appiumserver import AppiumServer as server

list_devices = os.path.dirname(os.path.abspath('.')) + '\\Phone\\devices.yaml'
ga = getYamlData.getYaml(list_devices)

class LoginTest(unittest.TestCase):
    '''《登录功能》'''

    @classmethod
    def setUpClass(cls):
        log.critical("--------------------登录功能测试开始--------------------")
        server.appiumServer(ga).startServer()
        sleep(10)

    def setUp(self):
        self.driver = GetPhoneInfo.AutoGetPhoneInfo().get_driver()
        self.Page = Z1_Login_page.LoginPage(self.driver)
        self.base = Common.Action(self.driver)
        self.createpng = CreatePng.CreatePNG(self.driver)

    # @ScreenAssert.decorator
    # def test_login_001(self):
    #     '''截图对比登录页面LOGO以及字样'''
    #     self.Page.click_video()
    #     self.Page.click_start()
    #     self.base.is_display_loc(self.Page.username_loc)
    #     self.createpng.CreateCustomSizeNowPNG('test_login_001',0,72,1080,700)
    #     old = self.base.gerLocOld('test_login_001')
    #     now = self.base.getLocNow('test_login_001')
    #     self.assertEqual(old,now)

    # @ScreenAssert.decorator
    # def test_login_002(self):
    #     '''截图对比登录页面'''
    #     self.Page.click_video()
    #     self.Page.click_start()
    #     self.base.is_display_loc(self.Page.username_loc)
    #     self.createpng.CreateCustomSizeNowPNG('test_login_002',0,840,1080,1776)
    #     old = self.base.gerLocOld('test_login_002')
    #     now = self.base.getLocNow('test_login_002')
    #     self.assertEqual(old,now)
    #
    # @ScreenAssert.decorator
    # def test_login_003(self):
    #     '''空账号'''
    #     self.Page.login('', 'aa111111')
    #     self.assertFalse(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/btn_login').is_enabled())

    @ScreenAssert.decorator
    def test_login_004(self):
        '''不存在的账号'''
        self.Page.login('shizwwwwwwwwwwwwww005', '11111111111')
        self.assertIsNotNone(self.base.find_toast('用户不存在', self.driver))
    #
    @ScreenAssert.decorator
    def test_login_005(self):
        '''账号为乱码'''
        self.Page.login('！@#￥%…………&*', '11111111111')
        self.assertIsNotNone(self.base.find_toast('用户不存在', self.driver))
    #
    # @ScreenAssert.decorator
    # def test_login_006(self):
    #     '''密码错误'''
    #     self.Page.login('zhangjgtest', '11111111111')
    #     self.assertIsNotNone(self.base.find_toast('密码错误', self.driver))
    #
    # @ScreenAssert.decorator
    # def test_login_007(self):
    #     '''密码为空'''
    #     self.Page.login('zhangjgtest', '')
    #     self.assertFalse(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/btn_login').is_enabled())
    #
    # @ScreenAssert.decorator
    # def test_login_008(self):
    #     '''登录成功'''
    #     self.Page.login('zhangjgtest', 'aa111111')
    #     self.assertIsNotNone(self.base.find_toast('登录成功', self.driver))
    #
    # @ScreenAssert.decorator
    # def test_login_009_qq(self):
    #     '''QQ登录'''
    #     self.Page.qq_login()
    #     self.assertIsNotNone(self.base.find_toast('登录成功', self.driver))
    #
    # @ScreenAssert.decorator
    # def test_login_010_wx(self):
    #     '''微信登录'''
    #     self.Page.wx_login()
    #     self.assertIsNotNone(self.base.find_toast('登录成功', self.driver))
    #
    # @ScreenAssert.decorator
    # def test_login_011_sina(self):
    #     '''微博登录'''
    #     self.Page.sina_login()
    #     self.assertIsNotNone(self.base.find_toast('登录成功', self.driver))

    def tearDown(self):
        sleep(3)
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        log.critical("--------------------登录功能测试结束--------------------")
        server.appiumServer(ga).stopServer()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    unittest.TextTestRunner(verbosity=2).run(suite)