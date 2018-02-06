import unittest
from time import sleep

from PO.po_page import B3_childdevice_page
from public import GetPhoneInfo, Common ,Log,CreatePng,ScreenAssert

log = Log.Logger(logger='Child_device').getLog()

class Child_device(unittest.TestCase):
    '''《孩子设备》'''

    @classmethod
    def setUpClass(cls):
        log.critical("--------------------孩子设备测试开始--------------------")

    def setUp(self):
        self.driver = GetPhoneInfo.Appium().driver()
        self.Page = B3_childdevice_page.child_device(self.driver)
        self.base = Common.Action(self.driver)
        self.png = CreatePng.CreatePNG(self.driver)

    @ScreenAssert.decorator
    def test_child_device_001(self):
        '''跳转孩子设备、返回用例'''
        self.Page.go_child_device()
        self.base.swipe_to_down(2, 4)
        try:
            self.assertIsNotNone(self.base.get_assert('id',self.Page.delete_btn_loc[1]))
        finally:
            self.Page.click_back_btn()
            self.assertIsNotNone(self.base.get_assert('xpath',self.Page.device_loc[1]))

    @ScreenAssert.decorator
    def test_child_device_002(self):
        '''检查孩子设备页面所有默认值'''
        self.Page.go_child_device()
        try:
            self.png.CreateCustomSizeNowPNG('test_child_device_002_1',0,72,1047,1711)
            self.assertEqual(self.base.gerLocOld('test_child_device_002_1'),self.base.getLocNow('test_child_device_002_1'))
        finally:
            self.base.swipe_to_down(2, 4)
            self.png.CreateCustomSizeNowPNG('test_child_device_002_2',0,72,1047,1711)
            self.assertEqual(self.base.gerLocOld('test_child_device_002_2'),self.base.getLocNow('test_child_device_002_2'))

    @ScreenAssert.decorator
    def test_child_device_003(self):
        '''检查孩子设备更换头像弹窗，截图对比，文本对比--跳转相机、图库未实现'''
        self.Page.go_child_device()
        self.Page.click_head_title()
        try:
            self.assertEqual(self.base.get_assert('xpath', self.Page.camera_loc[1]).text,"拍摄新照片")
            self.assertEqual(self.base.get_assert('xpath', self.Page.photo_loc[1]).text,"从相册选择")
        finally:
            try:
                self.png.CreateCustomSizeNowPNG('test_child_device_003',81,595,999,1255)
                self.assertEqual(self.base.gerLocOld('test_child_device_003'),self.base.getLocNow('test_child_device_003'))
            finally:
                self.Page.click_head_cancel()
                self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_title').text,"设备详情")

    @ScreenAssert.decorator
    def test_child_device_004(self):
        '''修改设备名称'''
        self.Page.go_child_device()
        try:
            self.Page.click_device_title()
            self.Page.input_text_btn(' ')
            self.Page.click_pwd_positive_btn()
            self.assertIsNotNone(self.base.find_toast("设备名称不能为空!",self.driver))
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_device_title').text, 'ZTE B2015')
        finally:
            self.Page.click_device_title()
            self.Page.input_text_btn('1234567890绿网天下巨头之一哈哈')
            self.Page.click_pwd_positive_btn()
            self.assertIsNotNone(self.base.find_toast("修改成功",self.driver))
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_device_title').text, '1234567890绿网天下巨...')

    @ScreenAssert.decorator
    def test_child_device_005(self):
        '''修改孩子设备手机号码'''
        self.Page.go_child_device()
        try:
            self.Page.check_child_phone('')
            self.assertIsNotNone(self.base.find_toast("号码不能为空",self.driver))
            self.assertEqual(self.base.get_assert('id', self.Page.device_phone_loc[1]).text, '未获取')
        finally:
            try:
                self.Page.check_child_phone('绿网18521524172')
                self.assertIsNotNone(self.base.find_toast("手机号码格式输入有误",self.driver))
                self.assertEqual(self.base.get_assert('id', self.Page.device_phone_loc[1]).text, '未获取')
            finally:
                self.Page.check_child_phone('18521524172')
                self.assertIsNotNone(self.base.find_toast("修改成功",self.driver))
                self.assertEqual(self.base.get_assert('id',self.Page.device_phone_loc[1]).text, '18521524172')

    @ScreenAssert.decorator
    def test_child_device_006(self):
        '''修改小主性别'''
        self.Page.go_child_device()
        self.base.swipe_to_down(2,4)
        try:
            self.Page.click_child_sex()
            self.Page.click_boy_btn()
            self.assertEqual(self.base.get_assert('id', self.Page.child_sex_loc[1]).text, '男')
        finally:
            self.Page.click_child_sex()
            self.Page.click_girl_btn()
            self.assertEqual(self.base.get_assert('id', self.Page.child_sex_loc[1]).text, '女')

    @ScreenAssert.decorator
    def test_child_device_007(self):
        '''小主出生年月滑动选择'''
        self.Page.go_child_device()
        self.Page.swipe_one_birth_down()
        self.assertEqual(self.base.get_assert('id', self.Page.child_birth_loc[1]).text, '2001-2')

    @ScreenAssert.decorator
    def test_child_device_008(self):
        '''小主年级滑动选择'''
        self.Page.go_child_device()
        self.Page.swipe_one_grade_down()
        self.assertEqual(self.base.get_assert('id', self.Page.child_grade_loc[1]).text, '二年级')

    @ScreenAssert.decorator
    def test_child_device_009(self):
        '''我是孩子滑动选择'''
        self.Page.go_child_device()
        self.Page.swipe_one_guardian_down()
        self.assertEqual(self.base.get_assert('id', self.Page.child_guardian_loc[1]).text, '妈妈')

    @ScreenAssert.decorator
    def test_child_device_097(self):
        '''检查取消删除设备功能'''
        self.Page.go_child_device()
        self.base.swipe_to_down(2,4)
        try:
            self.Page.click_delete_btn()
            sleep(2)
            self.assertIsNotNone(self.base.get_assert('id', self.Page.positive_btn_loc[1]))
        finally:
            self.Page.click_negative_btn()
            sleep(2)
            self.assertIsNotNone(self.base.get_assert('id', self.Page.delete_btn_loc[1]))

    @ScreenAssert.decorator
    def test_child_device_098(self):
        '''检查删除设备密码功能、删除设备功能'''
        self.Page.go_child_device()
        self.base.swipe_to_down(2,4)
        try:
            self.Page.click_delete_btn()
            sleep(2)
            self.Page.click_positive_btn()
            self.Page.input_text_btn(' ')
            self.Page.click_pwd_positive_btn()
            self.assertIsNotNone(self.base.find_toast("密码错误，请重新输入！", self.driver))
        finally:
            self.Page.click_delete_btn()
            sleep(2)
            self.Page.click_positive_btn()
            self.Page.input_text_btn('aa111111')
            self.Page.click_pwd_positive_btn()
            self.assertIsNotNone(self.base.find_toast("删除成功", self.driver))

    @ScreenAssert.decorator
    def test_child_device_099(self):
        '''空的设备验证'''
        self.Page.go_child_device()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_title').text, '设备管理')

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        log.critical("--------------------孩子设备测试结束--------------------")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Child_device)
    unittest.TextTestRunner(verbosity=2).run(suite)