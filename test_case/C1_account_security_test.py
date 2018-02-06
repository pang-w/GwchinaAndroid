from PO.po_page import C1_account_page,Z1_Login_page
from public import GetPhoneInfo,Common,Log,CreatePng,ScreenAssert
import unittest

log = Log.Logger(logger='Account_Security').getLog()

class Account_Security(unittest.TestCase):
    '''《账号与安全》绘制图案密码锁未写'''
    @classmethod
    def setUpClass(cls):
        log.critical("--------------------账号与安全测试开始--------------------")

    def setUp(self):
        self.driver = GetPhoneInfo.AppiumTest().get_driver()
        self.Page = C1_account_page.AccountPage(self.driver)
        self.base = Common.Action(self.driver)
        self.png = CreatePng.CreatePNG(self.driver)

    @ScreenAssert.decorator
    def test_account_001(self):
        '''账号与安全页面跳转'''
        self.Page.click_setting()
        self.assertIsNotNone(self.base.get_assert('xpath', self.Page.account_loc[1]))

    @ScreenAssert.decorator
    def test_account_002(self):
        '''账号与安全页面默认值'''
        self.Page.click_setting()
        self.Page.click_account()
        self.png.CreateCustomSizeNowPNG('test_account_002',0,72,1080,1776)
        self.assertEqual(self.base.gerLocOld('test_account_002'),self.base.getLocNow('test_account_002'))

    @ScreenAssert.decorator
    def test_account_003(self):
        '''绑定手机密码弹窗'''
        self.Page.go_phone()
        try:
            self.assertIsNotNone(self.base.get_assert('id', self.Page.phone_positive_loc[1]))
        finally:
            self.Page.click_phone_negative()
            self.assertIsNotNone(self.base.get_assert('id', self.Page.logout_loc[1]))

    @ScreenAssert.decorator
    def test_account_004(self):
        '''绑定手机空密码、错误密码、乱码密码、正确密码'''
        self.Page.go_phone()
        try:
            self.Page.input_phone('')
            self.Page.click_phone_positive()
            self.base.is_display('id',self.Page.pwd_error_text[1])
            self.png.CreateCustomSizeNowPNG('test_account_004',81,748,999,1103)
            self.assertEqual(self.base.gerLocOld('test_account_004'),self.base.getLocNow('test_account_004'))

        finally:
            try:
                self.Page.check_phone_pwd('error')
                self.base.is_display('id', self.Page.pwd_error_text[1])
                self.png.CreateCustomSizeNowPNG('test_account_004_2', 81, 748, 999, 1103)
                self.assertEqual(self.base.gerLocOld('test_account_004'), self.base.getLocNow('test_account_004_2'))
            finally:
                try:
                    self.Page.check_phone_pwd('!@#$%^&')
                    self.base.is_display('id', self.Page.pwd_error_text[1])
                    self.png.CreateCustomSizeNowPNG('test_account_004_3', 81, 748, 999, 1103)
                    self.assertEqual(self.base.gerLocOld('test_account_004'),
                                     self.base.getLocNow('test_account_004_3'))
                finally:
                    self.Page.check_phone_pwd('aa111111')
                    self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/edit_new_phone').text,"请输入新的手机号码")

    @ScreenAssert.decorator
    def test_account_005(self):
        '''设置图案密码锁密码取消功能'''
        self.Page.go_pattern()
        self.Page.click_pattern_negative()
        self.assertEqual(self.base.get_assert('id',self.Page.logout_loc[1]).text,'退出登录')

    @ScreenAssert.decorator
    def test_account_006(self):
        '''设置图案密码锁空密码、错误密码、乱码密码、正确密码'''
        self.Page.go_pattern()
        try:
            self.Page.input_pattern('')
            self.Page.click_pattern_positive()
            self.base.is_display('id',self.Page.pwd_error_text[1])
            self.png.CreateCustomSizeNowPNG('test_account_006_1',81,748,999,1103)
            self.assertEqual(self.base.gerLocOld('test_account_006'),self.base.getLocNow('test_account_006_1'))
        finally:
            try:
                self.Page.check_pattern_pwd('error')
                self.base.is_display('id', self.Page.pwd_error_text[1])
                self.png.CreateCustomSizeNowPNG('test_account_006_2', 81, 748, 999, 1103)
                self.assertEqual(self.base.gerLocOld('test_account_006'), self.base.getLocNow('test_account_006_2'))
            finally:
                try:
                    self.Page.check_pattern_pwd('!@#$%^&')
                    self.base.is_display('id', self.Page.pwd_error_text[1])
                    self.png.CreateCustomSizeNowPNG('test_account_006_3', 81, 748, 999, 1103)
                    self.assertEqual(self.base.gerLocOld('test_account_006'),
                                     self.base.getLocNow('test_account_006_3'))
                finally:
                    self.Page.check_pattern_pwd('aa111111')
                    self.assertIsNotNone(self.base.get_assert('xpath', '//android.widget.TextView[@text="设置图案密码锁"]'))

    @ScreenAssert.decorator
    def test_account_007(self):
        '''修改密码跳转'''
        self.Page.go_change_pwd()
        self.assertIsNotNone(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/btn_action'))

    @ScreenAssert.decorator
    def test_account_008(self):
        '''修改密码输入非纯英文、数字密码'''
        self.Page.go_change_pwd()
        self.Page.check_change_pwd('aa111111','11111111','11111111')
        self.assertIsNotNone(self.base.find_toast('请输入8-16位非纯英文与非纯数字组合', self.driver))

    @ScreenAssert.decorator
    def test_account_009(self):
        '''修改密码输入两次不密码'''
        self.Page.go_change_pwd()
        self.Page.check_change_pwd('aa111111','aa222222','aa333333')
        self.assertIsNotNone(self.base.find_toast('两次输入密码不一致,请重新输入', self.driver))

    @ScreenAssert.decorator
    def test_account_010(self):
        '''修改密码输入错误原始密码'''
        self.Page.go_change_pwd()
        self.Page.check_change_pwd('aaxxxxxx','aa222222','aa222222')
        self.assertIsNotNone(self.base.find_toast('密码不正确', self.driver))

    @ScreenAssert.decorator
    def test_account_011(self):
        '''修改密码输入密码与原密码相同'''
        self.Page.go_change_pwd()
        self.Page.check_change_pwd('aa111111','aa111111','aa111111')
        self.assertIsNotNone(self.base.find_toast('输入密码与原密码相同，请重新输入', self.driver))

    @ScreenAssert.decorator
    def test_account_012(self):
        '''修改密码成功'''
        self.Page.go_change_pwd()
        self.Page.check_change_pwd('aa111111', 'aa222222', 'aa222222')
        self.assertIsNotNone(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/ed_username'))
        Z1_Login_page.LoginPage(self.driver).login_page('18521524172', 'aa222222')
        self.assertIsNotNone(self.base.find_toast('登录成功', self.driver))
        self.Page.go_change_pwd()
        self.Page.check_change_pwd('aa222222', 'aa111111', 'aa111111')
        self.base.is_display('id','com.gwchina.lssw.parent:id/ed_username')
        Z1_Login_page.LoginPage(self.driver).login_page('18521524172', 'aa111111')
        self.base.is_display('xpath','//android.widget.TextView[@text="网址管理"]')

    @ScreenAssert.decorator
    def test_account_099(self):
        '''退出登录功能'''
        self.Page.check_logout()
        self.assertIsNotNone(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/btn_positive'))
        self.Page.click_logout_negative()
        self.assertIsNotNone(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/btn_logout'))
        self.Page.click_logout()
        self.Page.click_logout_positive()
        self.assertIsNotNone(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/ed_username'))

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        log.critical("--------------------账号与安全测试结束--------------------")

if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(Account_Security("test_account_10"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(Account_Security)
    unittest.TextTestRunner(verbosity=2).run(suite)

