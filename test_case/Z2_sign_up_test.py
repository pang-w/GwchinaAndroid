import unittest
from public import GetPhoneInfo, Common,Log,ScreenAssert
from PO.po_page import Z2_sign_up_page
from time import sleep

log = Log.Logger(logger='SignUpTest').getLog()

class SignUpTest(unittest.TestCase):
    '''登录页面注册功能'''

    @classmethod
    def setUpClass(cls):
        log.critical("--------------------登录页面注册功能测试开始--------------------")

    def setUp(self):
        self.driver = GetPhoneInfo.Appium().driverClear()
        self.Page = Z2_sign_up_page.LoginPage(self.driver)
        self.base = Common.Action(self.driver)

    @ScreenAssert.decorator
    def test_signup_001_phone(self):
        '''验证进入立即注册页面功能'''
        self.Page.go_register_page()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_title').text,"注册")

    @ScreenAssert.decorator
    def test_signup_002_phone(self):
        '''验证立即注册页面返回功能'''
        self.Page.go_register_page()
        self.Page.click_all_back_btn()
        self.assertIsNotNone(self.base.get_assert('id','com.gwchina.lssw.parent:id/ed_username'), 'error')

    @ScreenAssert.decorator
    def test_signup_003_phone(self):
        '''验证立即注册页面默认值'''
        self.Page.go_register_page()
        try:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/edit_username').text, "请输入家长手机号码")
        finally:
            try:
                self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/edit_valid_code').text,
                                 "请输入验证码")
            finally:
                try:
                    self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_tip_password').text,
                                     "请输入8-16位英文与数字组合")
                finally:
                    try:
                        self.assertFalse(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/btn_valid_code').is_enabled())
                    finally:
                        self.assertFalse(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/btn_register').is_enabled())

    @ScreenAssert.decorator
    def test_signup_004_phone(self):
        '''输入不足11的手机号验证'''
        self.Page.go_register_page()
        self.Page.input_re_username('11111111')
        self.Page.click_code_btn()
        self.assertIsNotNone(self.base.find_toast('请输入正确的手机号码', self.driver))

    @ScreenAssert.decorator
    def test_signup_005_phone(self):
        '''输入英文手机号验证'''
        self.Page.go_register_page()
        self.Page.input_re_username('aaaaaaa')
        self.Page.click_code_btn()
        self.assertIsNotNone(self.base.find_toast('请输入正确的手机号码', self.driver))

    @ScreenAssert.decorator
    def test_signup_006_phone(self):
        '''输入乱码手机号验证'''
        self.Page.go_register_page()
        self.Page.input_re_username('!@#$%^')
        self.Page.click_code_btn()
        self.assertIsNotNone(self.base.find_toast('请输入正确的手机号码', self.driver))

    @ScreenAssert.decorator
    def test_signup_007_phone(self):
        '''输入中文手机号验证'''
        self.Page.go_register_page()
        self.Page.input_re_username('测试')
        self.Page.click_code_btn()
        self.assertIsNotNone(self.base.find_toast('请输入正确的手机号码', self.driver))

    @ScreenAssert.decorator
    def test_signup_008_phone(self):
        '''输入已注册的手机号验证'''
        self.Page.go_register_page()
        self.Page.input_re_username('18521524172')
        self.Page.click_code_btn()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_account_exit').text,"账号已注册")

    @ScreenAssert.decorator
    def test_signup_009_phone(self):
        '''输入未注册的手机号'''
        self.Page.go_register_page()
        self.Page.input_re_username('18588888819')
        self.Page.click_code_btn()
        try:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/message').text,'验证码已发送至18588888819，请注意接收，验证码将在3分钟内有效。')
        finally:
            self.Page.click_iknow_btn()
            self.assertFalse(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/btn_valid_code').is_enabled())

    @ScreenAssert.decorator
    def test_signup_010_phone(self):
        '''输入错误的验证码'''
        self.Page.go_register_page()
        self.Page.input_re_username('18544433332')
        self.Page.click_code_btn()
        self.Page.click_iknow_btn()
        self.Page.input_code('1234')
        self.Page.input_new_pwd('aa111111')
        self.Page.click_confirm_register_btn()
        self.assertIsNotNone(self.base.find_toast('验证码输入错误，请重新输入', self.driver))

    @ScreenAssert.decorator
    def test_signup_011_email(self):
        '''切换至邮箱注册'''
        self.Page.go_mail_register_page()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/edit_username').text,'请输入邮箱号')

    @ScreenAssert.decorator
    def test_signup_012_email(self):
        '''邮箱注册返回'''
        self.Page.go_mail_register_page()
        self.Page.click_all_back_btn()
        self.assertIsNotNone(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/ed_username'),'error')

    @ScreenAssert.decorator
    def test_signup_013_email(self):
        '''切换至邮箱注册默认值'''
        self.Page.go_mail_register_page()
        try:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/edit_username').text, '请输入邮箱号')
        finally:
            try:
                self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/edit_valid_code').text, '请输入验证码')
            finally:
                try:
                    self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_tip_password').text,'请输入8-16位英文与数字组合')
                finally:
                    try:
                        self.assertFalse(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/btn_valid_code').is_enabled())
                    finally:
                        self.assertFalse(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/btn_register').is_enabled())

    @ScreenAssert.decorator
    def test_signup_014_email(self):
        '''输入错误格式的邮箱'''
        self.Page.go_mail_register_input('zhangjg@txtws.co')
        self.assertIsNotNone(self.base.find_toast('邮箱格式错误', self.driver))

    @ScreenAssert.decorator
    def test_signup_015_email(self):
        '''输入乱码邮箱'''
        self.Page.go_mail_register_input('~!@#$%&^*((&')
        self.assertIsNotNone(self.base.find_toast('邮箱格式错误', self.driver))

    @ScreenAssert.decorator
    def test_signup_016_email(self):
        '''输入中文邮箱'''
        self.Page.go_mail_register_input('绿网天下')
        self.assertIsNotNone(self.base.find_toast('邮箱格式错误', self.driver))

    @ScreenAssert.decorator
    def test_signup_017_email(self):
        '''输入已注册邮箱'''
        self.Page.go_mail_register_input('zhangjg@txtws.com')
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_account_exit').text,'邮箱已注册')

    @ScreenAssert.decorator
    def test_signup_018_email(self):
        '''输入正确的邮箱号'''
        self.Page.go_mail_register_input('zhangjg@163.com')
        try:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/message').text, '验证码已发送至zhangjg@163.com，请注意接收，验证码将在5分钟内有效。')
        finally:
            self.Page.click_iknow_btn()
            self.assertFalse(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/btn_valid_code').is_enabled())

    @ScreenAssert.decorator
    def test_signup_019_email(self):
        '''输入错误的验证码'''
        self.Page.go_mail_register_input('zhangjg@163.com')
        self.Page.click_iknow_btn()
        self.Page.input_code('1234')
        self.Page.input_new_pwd('aa111111')
        self.Page.input_new2_pwd('aa111111')
        self.Page.click_confirm_register_btn()
        self.assertIsNotNone(self.base.find_toast('验证码输入错误，请重新输入', self.driver))

    @ScreenAssert.decorator
    def test_signup_020_account(self):
        '''进入账号注册页面'''
        self.Page.go_account_register_page()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/edit_username').text,'请输入账号')

    @ScreenAssert.decorator
    def test_signup_021_account(self):
        '''进入账号注册页面返回'''
        self.Page.go_account_register_page()
        self.Page.click_all_back_btn()
        self.assertIsNotNone(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/ed_username'))

    @ScreenAssert.decorator
    def test_signup_022_account(self):
        '''切换至账号注册默认值'''
        self.Page.go_account_register_page()
        try:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/edit_username').text, '请输入账号')
        finally:
            try:
                self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_tip_username').text, '账号为纯数字或纯字母或数字字母组合')
            finally:
                try:
                    self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_tip_password').text,
                                     '请输入8-16位英文与数字组合')
                finally:
                    self.assertFalse(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/btn_register').is_enabled())

    @ScreenAssert.decorator
    def test_signup_023_account(self):
        '''输入乱码账号'''
        self.Page.go_account_register_page()
        self.Page.input_account_value('！@#￥%……&*', 'aa111111', 'aa111111')
        self.assertIsNotNone(self.base.find_toast('账号格式错误', self.driver))

    @ScreenAssert.decorator
    def test_signup_024_account(self):
        '''输入不足长度账号'''
        self.Page.go_account_register_page()
        self.Page.input_account_value('绿网天下', 'aa111111', 'aa111111')
        self.assertIsNotNone(self.base.find_toast('账号长度错误，请输入6-20位账号', self.driver))

    @ScreenAssert.decorator
    def test_signup_025_account(self):
        '''输入邮箱账号'''
        self.Page.go_account_register_page()
        self.Page.input_account_value('zhangjg@txtws.com', 'aa111111', 'aa111111')
        self.assertIsNotNone(self.base.find_toast('账号格式错误', self.driver))

    @ScreenAssert.decorator
    def test_signup_026_account(self):
        '''输入中文账号'''
        self.Page.go_account_register_page()
        self.Page.input_account_value('绿网天下上海分公司', 'aa111111', 'aa111111')
        self.assertIsNotNone(self.base.find_toast('账号格式错误', self.driver))

    @ScreenAssert.decorator
    def test_signup_027_account(self):
        '''输入已注册的账号'''
        self.Page.go_account_register_page()
        self.Page.input_account_value('zhangjg', 'aa111111', 'aa111111')
        self.assertIsNotNone(self.base.find_toast('账号已被注册', self.driver))

    @ScreenAssert.decorator
    def test_signup_028_account(self):
        '''输入正常格式的错误密码组合'''
        self.Page.go_account_register_page()
        self.Page.input_account_value('zhangjglvwangtianxia', 'aa111111', 'aa222222')
        self.assertIsNotNone(self.base.find_toast('两次输入密码不一致,请重新输入', self.driver))

    @ScreenAssert.decorator
    def test_signup_029_account(self):
        '''输入纯数字的密码组合'''
        self.Page.go_account_register_page()
        self.Page.input_account_value('zhangjglvwangtianxia', '11111111', '11111111')
        self.assertIsNotNone(self.base.find_toast('请输入8-16位非纯英文与非纯数字组合', self.driver))

    @ScreenAssert.decorator
    def test_signup_030_account(self):
        '''输入纯英文密码组合'''
        self.Page.go_account_register_page()
        self.Page.input_account_value('zhangjglvwangtianxia', 'aaaaaaaa', 'aaaaaaaa')
        self.assertIsNotNone(self.base.find_toast('请输入8-16位非纯英文与非纯数字组合', self.driver))

    @ScreenAssert.decorator
    def test_signup_031_account(self):
        '''输入不足6位密码组合'''
        self.Page.go_account_register_page()
        self.Page.input_account_value('zhangjglvwangtianxia', '1111', '1111')
        self.assertIsNotNone(self.base.find_toast('请输入8-16位非纯英文与非纯数字组合', self.driver))

    def tearDown(self):
        sleep(1)
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        log.critical("--------------------登录页面注册功能测试结束--------------------")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
    unittest.TextTestRunner(verbosity=2).run(suite)