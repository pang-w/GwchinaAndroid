import unittest

from PO.po_page import B9_about_us_page
from public import GetPhoneInfo, Common,Log,CreatePng,ScreenAssert
from time import sleep

log = Log.Logger(logger='About_Us').getLog()

class About_Us(unittest.TestCase):
    '''《关于我们》未实现：邮箱跳转第三方，服务热线跳转拨号,免责声明内容'''

    @classmethod
    def setUpClass(cls):
        log.critical("--------------------关于我们测试开始--------------------")

    def setUp(self):
        self.driver = GetPhoneInfo.Appium().driver()
        self.Page = B9_about_us_page.About_us(self.driver)
        self.base = Common.Action(self.driver)
        self.png = CreatePng.CreatePNG(self.driver)

    @ScreenAssert.decorator
    def test_about_001(self):
        '''验证关于我们页面LOGO显示，截图对比'''
        self.Page.go_about_us()
        self.png.CreateCustomSizeNowPNG('test_about_001',270,288,558,576)
        self.assertEqual(self.base.gerLocOld('test_about_001'),self.base.getLocNow('test_about_001'))

    @ScreenAssert.decorator
    def test_about_002(self):
        '''验证关于我们页面邮箱联系、服务热线、免责声明、加入官方QQ群、绿网天下（福建）网络科技股份有限公司闽ICP备09010660号，截图对比'''
        self.Page.go_about_us()
        self.base.swipe_to_down(1.2, 10)
        self.png.CreateCustomSizeNowPNG('test_about_002',57,817,1080,1776)
        self.assertEqual(self.base.gerLocOld('test_about_002'),self.base.getLocNow('test_about_002'))

    @ScreenAssert.decorator
    def test_about_003(self):
        '''验证检测版本，toast版本检测中...'''
        self.Page.go_about_us()
        self.Page.click_check_version()
        self.assertIsNotNone(self.base.find_toast("版本检测中...", self.driver))

    @ScreenAssert.decorator
    def test_about_004(self):
        '''验证格雷盒子名称以及版本'''
        self.Page.go_about_us()
        try:
            self.assertEqual(self.base.get_assert('id',self.Page.default_about_title_loc[1]).text,'格雷盒子')
        finally:
            self.assertEqual(self.base.get_assert('id', self.Page.default_version_loc[1]).text, 'V6.0.0')

    @ScreenAssert.decorator
    def test_about_005(self):
        '''验证关于我们版本说明弹窗显示，截图对比，查找按钮'''
        self.Page.go_about_us()
        self.Page.click_version()
        try:
            self.png.CreateCustomSizeNowPNG('test_about_005',81,350,999,533)
            self.assertEqual(self.base.gerLocOld('test_about_005'),self.base.getLocNow('test_about_005'))
            self.assertEqual(self.base.get_assert('id',self.Page.i_know_btn[1]).text,'我知道了')
        finally:
            self.Page.click_i_know()
            self.assertIsNotNone(self.base.get_assert('xpath', self.Page.version_loc[1]))

    @ScreenAssert.decorator
    def test_about_006(self):
        '''验证关于我们服务热线弹窗显示，截图对比，取消功能，确定功能未实现'''
        self.Page.go_about_us()
        self.Page.click_hotline()
        try:
            self.png.CreateCustomSizeNowPNG('test_about_006',81,703,999,1148)
            self.assertEqual(self.base.gerLocOld('test_about_006'),self.base.getLocNow('test_about_006'))
        finally:
            self.Page.click_phone_negative()
            self.assertIsNotNone(self.base.get_assert('xpath', self.Page.version_loc[1]))

    @ScreenAssert.decorator
    def test_about_007(self):
        '''验证关于我们免责声明页面显示，截图对比，取消功能，确定功能未实现'''
        self.Page.go_about_us()
        self.Page.click_mzsm()
        try:
            self.png.CreateCustomSizeNowPNG('test_about_007_1',0,72,1032,1108)
            self.assertEqual(self.base.gerLocOld('test_about_007_1'),self.base.getLocNow('test_about_007_1'))
        finally:
            try:
                url_text = self.base.get_assert('id',self.Page.http_value_loc[1]).text
                print(url_text)
                if url_text == 'http://home.cs.gwchina.cn/':
                    # self.base.swipe_to_down(2, 4)
                    self.png.CreateCustomSizeNowPNG('test_about_007_2',0,1196,1080,1698)
                    self.assertEqual(self.base.gerLocOld('test_about_007_2'),self.base.getLocNow('test_about_007_2'))
                elif url_text == 'http://home.gwchina.cn/':
                    # self.base.swipe_to_down(2, 4)
                    self.png.CreateCustomSizeNowPNG('test_about_007_3',0,1196,1080,1698) #图片未更新
                    self.assertEqual(self.base.gerLocOld('test_about_007_3'),self.base.getLocNow('test_about_007_3'))
            finally:
                self.Page.click_back()
                self.assertIsNotNone(self.base.get_assert('xpath', self.Page.version_loc[1]))

    @ScreenAssert.decorator
    def test_about_008(self):
        '''验证关于我们免责声明-用户协议页面显示，截图对比，返回功能'''
        self.Page.go_about_us()
        self.Page.click_mzsm()
        self.Page.click_agreement()
        try:
            sleep(5)
            self.png.CreateCustomSizeNowPNG('test_about_008',0,72,1000,1776)
            self.assertEqual(self.base.gerLocOld('test_about_008'), self.base.getLocNow('test_about_008'))
        finally:
            self.Page.click_back()
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_title').text,'免责声明')

    @ScreenAssert.decorator
    def test_about_009(self):
        '''验证关于我们返回功能'''
        self.Page.go_about_us()
        self.Page.click_back()
        self.assertIsNotNone(self.base.get_assert('xpath',self.Page.about_us_loc[1]))

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        log.critical("--------------------关于我们测试结束--------------------")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(About_Us)
    unittest.TextTestRunner(verbosity=2).run(suite)