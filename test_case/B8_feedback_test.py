import unittest
from PO.po_page import B8_feedback_page
from public import GetPhoneInfo,Common,Log,CreatePng,ScreenAssert

log = Log.Logger(logger='FeedBack').getLog()

class FeedBack(unittest.TestCase):
    '''《意见反馈》'''

    @classmethod
    def setUpClass(cls):
        log.critical("--------------------意见反馈测试开始--------------------")

    def setUp(self):
        self.driver = GetPhoneInfo.AppiumTest().get_driver()
        self.Page = B8_feedback_page.config(self.driver)
        self.base = Common.Action(self.driver)
        self.png = CreatePng.CreatePNG(self.driver)

    @ScreenAssert.decorator
    def test_feedback_001(self):
        '''意见反馈页面跳转'''
        self.Page.go_feedback()
        self.assertIsNotNone(self.base.get_assert('id',self.Page.submit_loc[1]))

    @ScreenAssert.decorator
    def test_feedback_002(self):
        '''意见反馈下半个页面截图对比默认值'''
        self.Page.go_feedback()
        self.png.CreateCustomSizeNowPNG('test_feedback_002',36,855,1080,1511)
        self.assertEqual(self.base.gerLocOld('test_feedback_002'),self.base.getLocNow('test_feedback_002'))

    @ScreenAssert.decorator
    def test_feedback_003(self):
        '''反馈意见不能为空提交'''
        self.Page.go_feedback()
        self.Page.input_msg(' ', ' ')
        self.assertIsNotNone(self.base.find_toast("反馈意见不能为空",self.driver))

    @ScreenAssert.decorator
    def test_feedback_004(self):
        '''联系方式不能为空提交'''
        self.Page.go_feedback()
        self.Page.input_msg('zhangjg', '')
        self.assertIsNotNone(self.base.find_toast("联系方式不能为空", self.driver))

    @ScreenAssert.decorator
    def test_feedback_005(self):
        '''错误联系方式提交'''
        self.Page.go_feedback()
        self.Page.input_msg('zhangjg', 'zhangjgtest')
        self.assertIsNotNone(self.base.find_toast("输入格式有误或不是常用邮箱，请重新输入", self.driver))

    @ScreenAssert.decorator
    def test_feedback_006(self):
        '''邮箱提交'''
        self.Page.go_feedback()
        self.Page.input_msg('zhangjgtestzhangjgtest', 'zhangjgtest@qq.com')
        self.assertIsNotNone(self.base.get_assert('xpath', self.Page.feedback_loc[1]))

    @ScreenAssert.decorator
    def test_feedback_007(self):
        '''手机号提交'''
        self.Page.go_feedback()
        self.Page.input_msg('zhangjgtestzhangjgtest', '18512345678')
        self.assertIsNotNone(self.base.get_assert('xpath', self.Page.feedback_loc[1]))

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        log.critical("--------------------意见反馈测试结束--------------------")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FeedBack)
    unittest.TextTestRunner(verbosity=2).run(suite)