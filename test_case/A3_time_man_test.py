import unittest
from time import sleep
from PO.po_page import A3_time_man_page
from public import Common,GetPhoneInfo,CreatePng,Log,ScreenAssert

log = Log.Logger(logger='TimeTest').getLog()

class TimeTest(unittest.TestCase):
    '''《时间管理》'''
    @classmethod
    def setUpClass(cls):
        log.critical("--------------------时间管理测试开始--------------------")

    def setUp(self):
        self.driver = GetPhoneInfo.Appium().driver()
        self.page = A3_time_man_page.time_page(self.driver)
        self.png = CreatePng.CreatePNG(self.driver)
        self.base = Common.Action(self.driver)

    @ScreenAssert.decorator
    def test_time_A001(self):
        '''首次进入时间管理验证引导页显示'''
        self.page.click_time_btn()
        self.base.is_display(self.page.Guide_confirm_page_btn[1])
        self.png.CreateCustomSizeNowPNG('test_time_001',0,490,1080,1350)
        self.assertEqual(self.base.gerLocOld('test_time_001'),self.base.getLocNow('test_time_001'))

    @ScreenAssert.decorator
    def test_time_A002(self):
        '''进入时间管理验证引导页查看更多页面显示'''
        self.page.click_time_btn()
        self.page.click_more()
        sleep(3)
        self.png.CreateCustomSizeNowPNG('test_time_002',0,72,1080,1776)
        self.assertEqual(self.base.gerLocOld('test_time_002'),self.base.getLocNow('test_time_002'))
        self.page.click_back()
        self.page.click_save()
        self.page.click_save_positive()
        self.base.is_display(self.page.save_btn[1])

    @ScreenAssert.decorator
    def test_time_A003(self):
        '''find_toast时间段更新成功'''
        self.page.click_time_btn()
        self.page.click_save()
        self.page.click_save_positive()
        self.base.find_toast("时间段更新成功",self.driver)

    @ScreenAssert.decorator
    def test_time_A004(self):
        '''进入时间管理验证返回功能'''
        self.page.go_time_homepage()
        self.page.click_back()
        self.base.is_display(self.page.time_btn_loc[1])
        self.assertIsNotNone(self.base.get_assert('xpath','//android.widget.TextView[@text="软件管理"]'))

    @ScreenAssert.decorator
    def test_time_A005(self):
        '''进入时间管理验证是否进入当天周期'''
        self.page.go_time_homepage()
        self.base.is_display(self.page.back_btn[1])
        get_text = self.driver.find_element_by_id('com.gwchina.lssw.parent:id/title').text
        get_weekday = self.page.get_weekday()
        self.assertEqual(get_text,get_weekday)

    @ScreenAssert.decorator
    def test_time_A006(self):
        '''进入时间管理验证默认时段时间表显示，截图对比默认进入时间管理的周期页面，时间表和时段'''
        self.page.go_time_homepage()
        self.png.CreateCustomSizeNowPNG('test_time_006',0,548,1080,1273)
        self.assertEqual(self.base.gerLocOld('test_time_006'),self.base.getLocNow('test_time_006'))

    @ScreenAssert.decorator
    def test_time_A007(self):
        '''验证进入每天周期功能'''
        self.page.go_time_homepage()
        try:
            self.page.click_time_1()
            self.assertEqual(self.base.get_assert('id','com.gwchina.lssw.parent:id/title').text,'周一可用时段')
            self.assertEqual(self.base.get_assert('id','com.gwchina.lssw.parent:id/tv_title_useduration').text,'周一可用时长')
        finally:
            try:
                self.page.click_time_2()
                self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/title').text, '周二可用时段')
                self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_title_useduration').text,
                                 '周二可用时长')
            finally:
                try:
                    self.page.click_time_3()
                    self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/title').text, '周三可用时段')
                    self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_title_useduration').text,
                                     '周三可用时长')
                finally:
                    try:
                        self.page.click_time_4()
                        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/title').text, '周四可用时段')
                        self.assertEqual(
                            self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_title_useduration').text,
                            '周四可用时长')
                    finally:
                        try:
                            self.page.click_time_5()
                            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/title').text,
                                             '周五可用时段')
                            self.assertEqual(
                                self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_title_useduration').text,
                                '周五可用时长')
                        finally:
                            try:
                                self.page.click_time_6()
                                self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/title').text,
                                                 '周六可用时段')
                                self.assertEqual(
                                    self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_title_useduration').text,
                                    '周六可用时长')
                            finally:
                                self.page.click_time_7()
                                self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/title').text,
                                                 '周日可用时段')
                                self.assertEqual(
                                    self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_title_useduration').text,
                                    '周日可用时长')

    @ScreenAssert.decorator
    def test_time_A008(self):
        '''验证取消一行时间表，页面验证，06:00-24:00'''
        self.page.go_time_homepage()
        self.base.swipe_screen(200,600,1040,600,500)
        self.page.click_save()
        self.page.click_save_positive()
        self.base.is_display(self.page.time_1_btn[1])
        self.assertEqual(self.base.get_assert('id','com.gwchina.lssw.parent:id/tv_time').text,'06:00-24:00')

    # def test_time_A8(self):
    #     '''验证取消一行时间表，API验证'''
        # self.page.go_time_homepage()
        # self.base.swipe_screen(100,600,1000,600,5000)
        # self.page.click_save()
        # self.page.click_save_positive()
        # self.assertEqual(self.base.get_assert('id','com.gwchina.lssw.parent:id/tv_time').text,'06:00-24:00')

    @ScreenAssert.decorator
    def test_time_A009(self):
        '''验证跨行取消多行时间表，页面验证，19:00-24:00'''
        self.page.go_time_homepage()
        self.base.swipe_screen(200, 750, 200, 1000, 500)
        self.page.click_save()
        self.page.click_save_positive()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_time').text, '19:00-24:00')

    @ScreenAssert.decorator
    def test_time_A011(self):
        '''验证取消全部时间表，页面验证，全天禁用'''
        self.page.go_time_homepage()
        self.base.swipe_screen(330, 1000, 1040, 1000, 500)
        self.page.click_save()
        self.page.click_save_positive()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_time').text, '全天禁用')

    @ScreenAssert.decorator
    def test_time_A012(self):
        '''验证滑动添加一行时间段，页面验证，1-4，01:00-05:00'''
        self.page.go_time_homepage()
        self.base.swipe_screen(330, 600, 850, 600, 500)
        self.page.click_save()
        self.page.click_save_positive()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_time').text, '01:00-05:00')

    @ScreenAssert.decorator
    def test_time_A013(self):
        '''验证滑动添加跨行时间段，页面验证，01:00-05:00,    07:00-14:00'''
        self.page.go_time_homepage()
        self.base.swipe_screen(350, 750, 350, 890, 500)
        self.page.click_save()
        self.page.click_save_positive()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_time').text, '01:00-05:00,    07:00-14:00')

    @ScreenAssert.decorator
    def test_time_A014(self):
        '''验证重合滑动添加时间段，页面验证，先20-21，在18-24'''
        self.page.go_time_homepage()
        self.base.swipe_screen(530, 1000, 690, 1000, 500)
        self.base.swipe_screen(200, 1000, 1000, 1000, 500)
        self.page.click_save()
        self.page.click_save_positive()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_time').text, '01:00-05:00,    07:00-14:00,    18:00-24:00')

    @ScreenAssert.decorator
    def test_time_A015(self):
        '''验证滑动时间表竖行，页面验证， 0 - 18 ，00:00-24:00'''
        self.page.go_time_homepage()
        self.base.swipe_screen(200, 600, 200, 1040, 500)
        self.page.click_save()
        self.page.click_save_positive()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_time').text, '00:00-24:00')

    @ScreenAssert.decorator
    def test_time_A016(self):
        '''验证滑动全部取消时间表，页面验证， 0 - 23 ，全天禁用'''
        self.page.go_time_homepage()
        self.base.swipe_screen(200, 600, 1000, 1040, 500)
        self.page.click_save()
        self.page.click_save_positive()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_time').text, '全天禁用')

    @ScreenAssert.decorator
    def test_time_A017(self):
        '''验证滑动全部选择时间表，页面验证， 0 - 23 ，00:00-24:00'''
        self.page.go_time_homepage()
        self.base.swipe_screen(200, 600, 1000, 1040, 500)
        self.page.click_save()
        self.page.click_save_positive()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_time').text, '00:00-24:00')

    def tearDown(self):
        sleep(2)
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        log.critical("--------------------时间管理测试结束--------------------")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TimeTest)
    unittest.TextTestRunner(verbosity=2).run(suite)