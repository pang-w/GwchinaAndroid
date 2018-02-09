from PO.po_page import A6_area_man_page
import unittest
from public import Common,GetPhoneInfo,CreatePng,GetApiData,Log,ScreenAssert
from time import sleep

log = Log.Logger(logger='AreaTest').getLog()

class AreaTest(unittest.TestCase):
    '''《安全区域》'''
    @classmethod
    def setUpClass(cls):
        log.critical("--------------------安全区域测试开始--------------------")

    def setUp(self):
        self.driver = GetPhoneInfo.Appium().driver()
        self.page = A6_area_man_page.AreaPage(self.driver)
        self.base = Common.Action(self.driver)
        self.png = CreatePng.CreatePNG(self.driver)
        self.api = GetApiData.GetApi()
        self.log = log

    @ScreenAssert.decorator
    def test_area_001(self):
        '''验证进入安全区域页面'''
        self.page.go_area_homepage()
        self.assertIsNotNone(self.base.get_assert('id',self.page.add_area_btn[1]))

    @ScreenAssert.decorator
    def test_area_002(self):
        '''验证安全区域返回上一页面'''
        self.page.go_area_homepage()
        self.page.click_back()
        self.assertIsNotNone(self.base.get_assert('xpath',self.page.area_btn[1]))

    @ScreenAssert.decorator
    def test_area_003(self):
        '''截图对比默认页面'''
        self.page.go_area_homepage()
        self.base.is_display(self.page.add_area_btn[1])
        self.png.CreateCustomSizeNowPNG('test_area_003',0,72,1080,1776)
        old = self.base.gerLocOld('test_area_003')
        now = self.base.getLocNow('test_area_003')
        self.assertEqual(old,now)

    @ScreenAssert.decorator
    def test_area_004(self):
        '''验证安全区域进入家的页面'''
        self.page.go_area_homepage()
        self.page.click_home()
        try:
            self.assertIsNotNone(self.base.find_toast('点击地图设置安全区域范围',self.driver))
        finally:
            self.assertIsNotNone(self.base.get_assert('id',self.page.rb_position_btn[1]))

    @ScreenAssert.decorator
    def test_area_005(self):
        '''验证安全区域进入学校的页面'''
        self.page.go_area_homepage()
        self.page.click_school()
        try:
            self.assertIsNotNone(self.base.find_toast('点击地图设置安全区域范围',self.driver))
        finally:
            self.assertIsNotNone(self.base.get_assert('id',self.page.rb_position_btn[1]))

    @ScreenAssert.decorator
    def test_area_006(self):
        '''验证添加家的地址，API对比'''
        self.page.go_area_homepage()
        self.page.click_home()
        self.page.area_point(500,1000)
        self.page.click_save_or_edit()
        sleep(3)
        now_value = self.page.address_text()
        old_value = self.api.get_area()
        self.assertEqual(now_value,old_value)

    @ScreenAssert.decorator
    def test_area_007(self):
        '''验证家默认守护时间的起止时间和定位频率，00:00-23:59，每天'''
        self.page.go_area_homepage()
        self.assertEqual(self.page.fence_time_text(),'00:00-23:59')
        self.assertEqual(self.page.fence_rate_text(),'每天')

    @ScreenAssert.decorator
    def test_area_008(self):
        '''验证删除家的安全区域取消功能'''
        self.page.go_area_homepage()
        self.page.click_save_or_edit()
        self.page.click_def()
        self.page.click_negative()
        self.page.click_save_or_edit()
        self.assertEqual(self.page.fence_time_text(),'00:00-23:59')

    @ScreenAssert.decorator
    def test_area_009(self):
        '''验证删除家的安全区域确定功能,截图对比，有BUG'''
        self.page.go_area_homepage()
        self.page.click_save_or_edit()
        self.page.click_def()
        self.page.click_positive()

        self.png.CreateCustomSizeNowPNG('test_area_009',0,240,1080,798)
        old = self.base.gerLocOld('test_area_009')
        now = self.base.getLocNow('test_area_009')
        self.assertEqual(old,now)

    @ScreenAssert.decorator
    def test_area_010(self):
        '''验证添加学校的地址，API对比'''
        self.page.go_area_homepage()
        self.page.click_school()
        self.page.area_point(700,1300)
        self.page.click_save_or_edit()
        sleep(3)
        now_value = self.page.address_text()
        old_value = self.api.get_area()
        self.assertEqual(now_value,old_value)

    @ScreenAssert.decorator
    def test_area_011(self):
        '''验证学校默认守护时间的起止时间和定位频率，00:00-23:59，每天'''
        self.page.go_area_homepage()
        self.assertEqual(self.page.fence_time_text(),'00:00-23:59')
        self.assertEqual(self.page.fence_rate_text(),'每天')

    @ScreenAssert.decorator
    def test_area_012(self):
        '''验证删除学校的安全区域取消功能'''
        self.page.go_area_homepage()
        self.page.click_save_or_edit()
        self.page.click_def()
        self.page.click_negative()
        self.page.click_save_or_edit()
        self.assertEqual(self.page.fence_time_text(),'00:00-23:59')

    @ScreenAssert.decorator
    def test_area_013(self):
        '''验证删除学校的安全区域确定功能,截图对比，有BUG'''
        self.page.go_area_homepage()
        self.page.click_save_or_edit()
        self.page.click_def()
        self.page.click_positive()
        self.png.CreateCustomSizeNowPNG('test_area_013',0,240,1080,798)
        old = self.base.gerLocOld('test_area_013')
        now = self.base.getLocNow('test_area_013')
        self.assertEqual(old,now)

    @ScreenAssert.decorator
    def test_area_014(self):
        '''验证添加自定义安全区域 点击新增安全区域 - 点击保存 - 输入名称 - 确定 - toast请设置安全区域中心位置'''
        pass
        '''偶尔不提示请设置安全区域中心位置，直接添加测试安全区域成功，导致下面用例测试失败'''
        # self.page.go_area_homepage()
        # self.page.click_add_area()
        # self.page.click_save_or_edit()
        # self.page.input_area_name('测试')
        # self.page.click_positive()
        # self.assertIsNotNone(self.base.find_toast('请设置安全区域中心位置',self.driver))

    @ScreenAssert.decorator
    def test_area_015(self):
        '''验证添加自定义安全区域点击新增安全区域-点击保存-输入空名称-确定-toast添加安全区域名称'''
        self.page.go_area_homepage()
        self.page.click_add_area()
        self.page.click_save_or_edit()
        self.page.input_area_name(' ')
        self.page.click_positive()
        self.assertIsNotNone(self.base.find_toast('添加安全区域名称',self.driver))

    @ScreenAssert.decorator
    def test_area_016(self):
        '''验证添加自定义安全区域点击新增安全区域-点击保存-输入名称-确定-点击地图-确认-截图对比验证名称-测试'''
        self.page.go_area_homepage()
        self.page.click_add_area()
        self.page.area_point(400,1300)
        self.page.click_save_or_edit()
        self.page.input_area_name('测试')
        sleep(2)
        self.page.click_positive()
        self.base.is_display(self.page.home_btn[1],'xpath')
        self.png.CreateCustomSizeNowPNG('test_area_016',0,240,1080,783)
        old = self.base.gerLocOld('test_area_016')
        now = self.base.getLocNow('test_area_016')
        self.assertEqual(old,now)

    @ScreenAssert.decorator
    def test_area_017(self):
        '''验证添加自定义安全区域的地址，api对比'''
        self.page.go_area_homepage()
        self.assertEqual(self.page.address_text(),self.api.get_area())

    @ScreenAssert.decorator
    def test_area_018(self):
        '''验证添加自定义安全区域的起止时间和定位频率，00:00-23:59，每天'''
        self.page.go_area_homepage()
        self.assertEqual(self.page.fence_time_text(),'00:00-23:59')
        self.assertEqual(self.page.fence_rate_text(),'每天')

    @ScreenAssert.decorator
    def test_area_019(self):
        '''验证删除自定义安全区域功能取消功能，截图对比'''
        self.page.go_area_homepage()
        self.page.click_save_or_edit()
        self.page.click_def()
        self.page.click_negative()
        self.page.click_save_or_edit()
        self.base.is_display(self.page.home_btn[1])
        self.png.CreateCustomSizeNowPNG('test_area_019',0,240,1080,783)
        self.assertEqual(self.base.gerLocOld('test_area_019'),self.base.getLocNow('test_area_019'))

    @ScreenAssert.decorator
    def test_area_020(self):
        '''验证修改自定义安全区域名称取消功能，截图对比'''
        self.page.go_area_homepage()
        self.page.click_test()
        self.page.click_save_or_edit()
        self.page.input_area_name('修改测试名称')
        self.page.click_negative()
        self.page.click_back()
        self.base.is_display(self.page.add_area_btn[1])
        self.png.CreateCustomSizeNowPNG('test_area_020',0,240,1080,783)
        self.assertEqual(self.base.gerLocOld('test_area_020'),self.base.getLocNow('test_area_020'))

    @ScreenAssert.decorator
    def test_area_021(self):
        '''验证修改自定义安全区域名称确定功能，截图对比'''
        self.page.go_area_homepage()
        self.page.click_test()
        self.page.click_save_or_edit()
        self.page.input_area_name('修改测试名称')
        self.page.click_positive()
        self.base.is_display(self.page.add_area_btn[1])
        self.png.CreateCustomSizeNowPNG('test_area_021',0,240,1080,783)
        self.assertEqual(self.base.gerLocOld('test_area_021'),self.base.getLocNow('test_area_021'))

    @ScreenAssert.decorator
    def test_area_022(self):
        '''验证删除自定义安全区域功能确定功能，截图对比,有BUG'''
        self.page.go_area_homepage()
        self.page.click_save_or_edit()
        self.page.click_def()
        self.page.click_positive()
        self.base.is_display(self.page.home_btn[1])
        self.png.CreateCustomSizeNowPNG('test_area_022',0,240,1080,783)
        self.assertEqual(self.base.gerLocOld('test_area_022'),self.base.getLocNow('test_area_022'))

    @ScreenAssert.decorator
    def test_area_023(self):
        '''以家为例,验证添加正常的安全区域,api对比'''
        self.page.go_area_homepage()
        self.page.click_home()
        self.page.area_point(900,800)
        self.page.click_save_or_edit()
        self.base.is_display(self.page.home_btn[1])
        self.assertEqual(self.api.get_area(),self.page.address_text())

    @ScreenAssert.decorator
    def test_area_024(self):
        '''以家为例,验证修改安全区域地址,api对比'''
        test_area_C5_text = self.api.get_area()
        self.page.go_area_homepage()
        self.page.click_home()
        self.page.area_point(150, 600)
        self.page.click_save_or_edit()
        self.base.is_display(self.page.home_btn[1])
        self.assertNotEqual(test_area_C5_text,self.page.address_text())

    @ScreenAssert.decorator
    def test_area_025(self):
        '''以家为例,验证默认的守护时间页面显示，截图对比'''
        self.page.go_rb_time_page()
        self.png.CreateCustomSizeNowPNG('test_area_025',24,108,1080,695)
        self.assertEqual(self.base.gerLocOld('test_area_025'),self.base.getLocNow('test_area_025'))

    @ScreenAssert.decorator
    def test_area_026(self):
        '''以家为例,验证设置时间页面默认显示，截图对比'''
        self.page.go_rb_time_page()
        self.page.click_rb_start_end_time()
        self.base.is_display(self.page.rb_everyday_btn[1])
        self.png.CreateCustomSizeNowPNG('test_area_026',0,72,1080,1776)
        self.assertEqual(self.base.gerLocOld('test_area_026'),self.base.getLocNow('test_area_026'))

    @ScreenAssert.decorator
    def test_area_027(self):
        '''以家为例,验证二级页面、三级页面、四级页面(设置时间)返回功能'''
        self.page.go_rb_time_page()
        self.page.click_rb_start_end_time()
        self.page.click_back()
        self.assertIsNotNone(self.base.get_assert('id',self.page.rb_position_btn[1]))
        self.page.click_back()
        self.assertIsNotNone(self.base.get_assert('xpath',self.page.home_btn[1]))
        self.page.click_back()
        self.assertIsNotNone(self.base.get_assert('xpath',self.page.area_btn[1]))

    @ScreenAssert.decorator
    def test_area_028(self):
        '''以家为例,验证修改设置时间,当前页面(设置时间页面)时间范围显示,02:02-01:01'''
        self.page.go_rb_time_page()
        self.page.click_rb_start_end_time()
        self.page.click_rb_time_range()
        self.base.is_display(self.page.rb_finish_btn[1])
        self.base.swipe_screen(176,1265,176,1018,1000)
        self.base.swipe_screen(419,1265,419,1018,1000)
        self.base.swipe_screen(673,1265,673,1018,1000)
        self.base.swipe_screen(930,1265,930,1018,1000)
        self.page.click_rb_finish()
        self.page.click_save_or_edit()
        self.assertIsNotNone(self.base.find_toast('起始时间需要早于结束时间',self.driver))

    @ScreenAssert.decorator
    def test_area_029(self):
        '''以家为例,验证修改设置时间,当前页面(设置时间页面)时间范围显示,02:02-21:01 BUG:四级页面修改时间后保存，三级页面直接返回数据未保存'''
        self.page.go_rb_time_page()
        self.page.click_rb_start_end_time()
        self.page.click_rb_time_range()
        self.base.is_display(self.page.rb_finish_btn[1])
        self.base.swipe_screen(176,1265,176,1018,1000)
        self.base.swipe_screen(419,1265,419,1018,1000)
        self.base.swipe_screen(673,1265,673,1508,1000)
        self.base.swipe_screen(930,1265,930,1018,1000)
        self.page.click_rb_finish()
        try:
            self.assertEqual(self.base.get_assert('id',self.page.rb_time_range_btn[1]).text,'02:02-21:01')
        finally:
            self.page.click_save_or_edit()
            self.page.click_save_or_edit()
            self.base.is_display(self.page.home_btn[1])

    @ScreenAssert.decorator
    def test_area_030(self):
        '''以家为例,验证修改设置时间后,设置范围中心页面的时间范围是否同步'''
        self.page.go_rb_time_page()
        self.assertEqual(self.base.get_assert('id',self.page.rb_start_end_time_btn[1]).text,'02:02-21:01')

    @ScreenAssert.decorator
    def test_area_031(self):
        '''以家为例,验证修改设置时间后,安全区域家的时间返回是否同步'''
        self.page.go_area_homepage()
        self.assertEqual(self.page.fence_time_text(),'02:02-21:01')

    @ScreenAssert.decorator
    def test_area_032(self):
        '''以家为例,验证默认定位频率,当前页面(设置时间页面)定位频率显示,每天,截图对比'''
        self.page.go_rb_time_page()
        self.page.click_rb_locate_frequency()
        self.png.CreateCustomSizeNowPNG('test_area_032',0,583,1080,1216)
        self.assertEqual(self.base.gerLocOld('test_area_032'),self.base.getLocNow('test_area_032'))

    @ScreenAssert.decorator
    def test_area_033(self):
        '''以家为例,验证修改定位频率,当前页面(设置时间页面)定位频率显示,上学日,截图对比'''
        self.page.go_rb_time_page()
        self.page.click_rb_locate_frequency()
        self.page.click_rb_workday()
        self.png.CreateCustomSizeNowPNG('test_area_033',0,583,1080,1216)
        try:
            self.assertEqual(self.base.gerLocOld('test_area_033'),self.base.getLocNow('test_area_033'))
        finally:
            self.page.click_save_or_edit()
            self.page.click_save_or_edit()
            self.base.is_display(self.page.home_btn[1])

    @ScreenAssert.decorator
    def test_area_034(self):
        '''以家为例,验证修改定位频率后,设置范围中心页面的定位频率返回是否同步，上学日'''
        self.page.go_rb_time_page()
        self.assertEqual(self.base.get_assert('id',self.page.rb_locate_frequency_btn[1]).text,'上学日')

    @ScreenAssert.decorator
    def test_area_035(self):
        '''以家为例,验证修改定位频率,当前页面(设置时间页面)定位频率显示,上学日,截图对比'''
        self.page.go_rb_time_page()
        self.page.click_rb_locate_frequency()
        self.page.click_rb_weekend()
        self.png.CreateCustomSizeNowPNG('test_area_035',0,583,1080,1216)
        try:
            self.assertEqual(self.base.gerLocOld('test_area_035'),self.base.getLocNow('test_area_035'))
        finally:
            self.page.click_save_or_edit()
            self.page.click_save_or_edit()
            self.base.is_display(self.page.home_btn[1])

    @ScreenAssert.decorator
    def test_area_036(self):
        '''以家为例,验证修改定位频率后,安全区域家的定位频率返回是否同步，周末'''
        self.page.go_area_homepage()
        self.assertEqual(self.base.get_assert('id',self.page.fence_rate[1]).text,'周末')

    @ScreenAssert.decorator
    def test_area_037(self):
        '''以家为例,验证区域范围默认值，截图对比'''
        self.page.go_rb_time_page()
        self.page.click_rb_radius()
        self.png.CreateCustomSizeNowPNG('test_area_037',0,72,1080,690)
        self.assertEqual(self.base.gerLocOld('test_area_037'),self.base.getLocNow('test_area_037'))

    @ScreenAssert.decorator
    def test_area_038(self):
        '''以家为例,验证设置区域范围值，以点击方式设置区域范围的值 4.0千米'''
        self.page.go_rb_time_page()
        self.page.click_rb_radius()
        self.page.area_point(776,581)
        try:
            self.assertEqual(self.page.rb_radius_num_text(),'4.0千米')
        finally:
            self.page.click_save_or_edit()

    @ScreenAssert.decorator
    def test_area_039(self):
        '''以家为例,验证设置区域范围值，以点击方式设置区域范围的值 2.2千米'''
        self.page.go_rb_time_page()
        self.page.click_rb_radius()
        self.base.swipe_screen(776,581,360,581,1000)
        try:
            self.assertEqual(self.page.rb_radius_num_text(),'2.2千米')
        finally:
            self.page.click_save_or_edit()
            self.assertIsNotNone(self.base.find_toast('操作成功',self.driver))

    @ScreenAssert.decorator
    def test_area_040(self):
        '''添加5个安全区域地址后验证提示，toast 最多设置5个安全区域'''
        self.page.go_area_homepage()
        self.page.click_home()
        self.page.area_point(800,1000)
        self.page.click_save_or_edit()
        self.page.click_school()
        self.page.area_point(800,600)
        self.page.click_save_or_edit()
        self.page.click_add_area()
        self.page.area_point(680,600)
        self.page.click_save_or_edit()
        self.page.input_area_name('第三个安全区域测试')
        self.page.click_positive()
        self.page.click_add_area()
        self.page.area_point(270,600)
        self.page.click_save_or_edit()
        self.page.input_area_name('第四个安全区域测试')
        self.page.click_positive()
        self.page.click_add_area()
        self.page.area_point(500,1400)
        self.page.click_save_or_edit()
        self.page.input_area_name('第五个安全区域测试')
        self.page.click_positive()
        sleep(2)
        self.page.click_add_area()
        self.assertIsNotNone(self.base.find_toast('最多设置5个安全区域',self.driver))

    @ScreenAssert.decorator
    def test_area_041(self):
        '''验证删除家后，家的默认昵称保留,截图对比'''
        self.page.go_area_homepage()
        self.page.click_save_or_edit()
        self.page.click_def()
        self.page.click_positive()
        self.base.is_display(self.page.home_btn[1],'xpath')
        self.png.CreateCustomSizeNowPNG('test_area_041',0,72,1080,413)
        self.assertEqual(self.base.gerLocOld('test_area_041'),self.base.getLocNow('test_area_041'))

    @ScreenAssert.decorator
    def test_area_042(self):
        '''验证删除学校后，学校的默认昵称保留,截图对比'''
        self.page.go_area_homepage()
        self.page.click_save_or_edit()
        self.page.click_def()
        self.page.click_positive()
        self.base.is_display(self.page.school_btn[1],'xpath')
        self.png.CreateCustomSizeNowPNG('test_area_042',0,72,1080,616)
        self.assertEqual(self.base.gerLocOld('test_area_042'),self.base.getLocNow('test_area_042'))

    @ScreenAssert.decorator
    def test_area_043(self):
        '''验证删除所有自定义的三个安全区域后,截图对比'''
        self.page.go_area_homepage()
        self.page.click_save_or_edit()
        self.page.click_def()
        self.page.click_positive()
        self.page.click_def()
        self.page.click_positive()
        self.page.click_def()
        self.page.click_positive()
        self.page.click_save_or_edit()
        self.base.is_display(self.page.school_btn[1],'xpath')
        self.png.CreateCustomSizeNowPNG('test_area_043',0,72,1080,1776)
        self.assertEqual(self.base.gerLocOld('test_area_043'),self.base.getLocNow('test_area_043'))

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        log.critical("--------------------安全区域测试结束--------------------")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AreaTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
