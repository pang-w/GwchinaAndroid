from PO.po_page import A2_url_man_page
import unittest
from public import GetPhoneInfo,Common,CreatePng,Log,GetSQLData,ScreenAssert
from time import sleep

log = Log.Logger(logger='URL_Management').getLog()

class URL_Management(unittest.TestCase):
    '''《网址管理》'''
    @classmethod
    def setUpClass(cls):
        log.critical("--------------------网址管理测试开始--------------------")

    def setUp(self):
        self.driver = GetPhoneInfo.Appium().driver()
        self.Page = A2_url_man_page.url_page(self.driver)
        self.base = Common.Action(self.driver)
        self.png = CreatePng.CreatePNG(self.driver)
        self.sql = GetSQLData

    '''
    以下网址管理等级测试用例
    '''
    @ScreenAssert.decorator
    def test_url_A001_level(self):
        '''进入网址管理功能'''
        self.Page.go_url_homepage()
        self.assertEqual(self.base.get_assert('id','com.gwchina.lssw.parent:id/tv_title').text,"网址管理")

    @ScreenAssert.decorator
    def test_url_A002_level(self):
        '''进入网址管理验证返回功能'''
        self.Page.go_url_homepage()
        self.Page.click_back_btn()
        self.assertIsNotNone(self.base.get_assert('xpath','//android.widget.TextView[@text="软件管理"]'),'error')

    @ScreenAssert.decorator
    def test_url_A003_level(self):
        '''网址管理默认项'''
        self.Page.go_url_homepage()
        try:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/iv_expand').text, "收起")
        finally:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_hint').text, "标准 模式下，不允许孩子上网的类型")

    @ScreenAssert.decorator
    def test_url_A004_level(self):
        '''验证管理等级默认轻松'''
        self.Page.go_url_homepage()
        self.Page.click_level_low_btn()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_hint').text, "轻松 模式下，不允许孩子上网的类型")

    @ScreenAssert.decorator
    def test_url_A005_level(self):
        '''验证管理等级默认轻松,截图对比严格-标准-轻松区域显示'''
        self.Page.go_url_homepage()
        self.Page.click_level_low_btn()
        self.png.CreateCustomSizeNowPNG('test_url_A005_level',0,240,1080,1208)
        old = self.base.gerLocOld('test_url_A005_level')
        now = self.base.getLocNow('test_url_A005_level')
        self.assertEqual(old,now)

    @ScreenAssert.decorator
    def test_url_A006_level(self):
        '''验证管理等级切换至标准'''
        self.Page.go_url_homepage()
        self.Page.click_level_middle_btn()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_hint').text, "标准 模式下，不允许孩子上网的类型")

    @ScreenAssert.decorator
    def test_url_A007_level(self):
        '''验证管理等级切换至标准,截图对比严格-标准-轻松区域显示'''
        self.Page.go_url_homepage()
        self.Page.click_level_middle_btn()
        self.png.CreateCustomSizeNowPNG('test_url_A007_level', 0, 240, 1080, 1208)
        old = self.base.gerLocOld('test_url_A007_level')
        now = self.base.getLocNow('test_url_A007_level')
        self.assertEqual(old,now)

    @ScreenAssert.decorator
    def test_url_A008_level(self):
        '''验证管理等级切换至严格'''
        self.Page.go_url_homepage()
        self.Page.click_level_high_btn()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_hint').text, "严格 模式下，不允许孩子上网的类型")

    @ScreenAssert.decorator
    def test_url_A009_level(self):
        '''验证管理等级切换至严格,截图对比严格-标准-轻松区域显示'''
        self.Page.go_url_homepage()
        self.Page.click_level_high_btn()
        self.png.CreateCustomSizeNowPNG('test_url_A009_level', 0, 240, 1080, 1208)
        old = self.base.gerLocOld('test_url_A009_level')
        now = self.base.getLocNow('test_url_A009_level')
        self.assertEqual(old,now)

    @ScreenAssert.decorator
    def test_url_A010_level(self):
        '''验证管理等级收起/放开'''
        self.Page.go_url_homepage()
        self.Page.click_expand_btn()
        try:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/iv_expand').text, "更多设置")
        finally:
            self.Page.click_expand_btn()
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/iv_expand').text, "收起")

    @ScreenAssert.decorator
    def test_url_A011_level(self):
        '''验证切换至严格模式保存后，SQL对比{'url_limit_id': 1}'''
        self.Page.go_url_homepage()
        self.Page.click_level_high_btn()
        self.Page.click_save_or_delete_btn()
        sleep(2)
        self.assertEqual(self.sql.sql_url_limit_id(),{'url_limit_id': 1})

    @ScreenAssert.decorator
    def test_url_A012_level(self):
        '''验证切换至标准模式保存后，SQL对比{'url_limit_id': 2}'''
        self.Page.go_url_homepage()
        self.Page.click_level_middle_btn()
        self.Page.click_save_or_delete_btn()
        sleep(2)
        self.assertEqual(self.sql.sql_url_limit_id(),{'url_limit_id': 2})

    @ScreenAssert.decorator
    def test_url_A013_level(self):
        '''验证切换至轻松模式保存后，SQL对比{'url_limit_id': 3}'''
        self.Page.go_url_homepage()
        self.Page.click_level_low_btn()
        self.Page.click_save_or_delete_btn()
        sleep(2)
        self.assertEqual(self.sql.sql_url_limit_id(),{'url_limit_id': 3})

    '''
    以下网址黑名单测试用例
    '''
    @ScreenAssert.decorator
    def test_url_B001_black(self):
        '''验证黑名单默认页面，如何截取固定坐标的图片做对比，小格雷logo空空大'''
        self.Page.go_black_list()
        self.base.is_display('id',self.Page.save_btn_loc[1])
        self.png.CreateCustomSizeNowPNG('test_url_B001_black',0,72,1080,1776)
        self.assertEqual(self.base.gerLocOld('test_url_B001_black'),self.base.getLocNow('test_url_B001_black'))

    @ScreenAssert.decorator
    def test_url_B002_black(self):
        '''验证黑名单页面默认项'''
        self.Page.go_black_list()
        try:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_empty_tip').text, "空空哒~")
        finally:
            self.assertTrue(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/iv_back').is_enabled(), "error")

    @ScreenAssert.decorator
    def test_url_B003_black(self):
        '''验证添加黑名单网址默认值以及取消功能'''
        self.Page.go_url_homepage()
        self.Page.click_black_btn()
        self.Page.click_add_black_btn()
        try:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/title').text, "添加后孩子将不可访问该网址")
        finally:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/ed_nick').text, "www.xxx.com")

    @ScreenAssert.decorator
    def test_url_B004_black(self):
        '''验证添加黑名单网址取消功能'''
        self.Page.go_black_list()
        self.Page.click_add_black_btn()
        self.Page.click_popup_negative_btn()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_empty_tip').text, "空空哒~")

    @ScreenAssert.decorator
    def test_url_B005_black(self):
        '''验证添加黑名单网址清除字符功能'''
        self.Page.go_black_list()
        self.Page.click_add_black_btn()
        self.Page.input_popup_nick('1111111')
        self.Page.input_popup_nick_clear()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/ed_nick').text, "www.xxx.com")

    @ScreenAssert.decorator
    def test_url_B006_black(self):
        '''验证添加非法格式黑名单网址功能'''
        self.Page.go_black_list()
        try:
            self.Page.input_nick_value(' ')
            self.assertIsNotNone(self.base.find_toast("网址格式不正确",self.driver))
        finally:
            try:
                pass
                # self.Page.input_nick_value('www.baidu.co')
                # self.assertIsNotNone(self.base.find_toast("网址格式不正确",self.driver))
            finally:
                self.Page.input_nick_value('!@#$%^&*&')
                self.assertIsNotNone(self.base.find_toast("网址格式不正确", self.driver))

    @ScreenAssert.decorator
    def test_url_B007_black(self):
        '''添加百度网址，页面对比'''
        self.Page.add_black_url('baidu.com')
        try:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_name').text, "百度")
        finally:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_load_more').text, "— 加载完毕，共1条数据 —")
        self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_B008_black(self):
        '''验证编辑百度网址时，百度的名称和网址'''
        self.Page.add_black_url('baidu.com')
        self.Page.click_url_value()
        try:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/ed_nick_name').text, "百度")
        finally:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/ed_nick').text, "baidu.com")
        self.Page.click_popup_negative_btn()
        self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_B009_black(self):
        '''验证取消编辑百度网址功能'''
        self.Page.add_black_url('baidu.com')
        self.Page.click_url_value()
        self.Page.click_popup_negative_btn()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_url').text, "baidu.com")
        self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_B010_black(self):
        '''验证编辑黑名单网址输入非法格式的网址保存功能'''
        self.Page.add_black_url('baidu.com')
        self.Page.click_url_value()
        self.Page.input_popup_nick_name('')
        self.Page.click_popup_positive_btn()
        try:
            self.assertIsNotNone(self.base.find_toast("网址名称不能为空",self.driver))
        finally:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_url').text, "baidu.com")
        self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_B011_black(self):
        '''验证编辑黑名单网址输入正常的名称保存功能'''
        self.Page.add_black_url('baidu.com')
        self.Page.click_url_value()
        self.Page.input_popup_nick_name('你猜我猜不猜')
        self.Page.click_popup_positive_btn()
        try:
            self.assertIsNotNone(self.base.find_toast("操作成功",self.driver))
        finally:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_name').text, "你猜我猜不猜")
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_url').text, "baidu.com")
        self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_B012_black(self):
        '''验证编辑黑名单网址输入正常的名称和网址保存功能'''
        self.Page.add_black_url('baidu.com')
        self.Page.click_url_value()
        self.Page.input_popup_nick_name('绿网天下上海市分公司')
        self.Page.input_popup_nick_url('www.qq.com')
        self.Page.click_popup_positive_btn()
        try:
            self.assertIsNotNone(self.base.find_toast("操作成功",self.driver))
        finally:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_name').text, "绿网天下上海市分公司")
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_url').text, "qq.com")
        self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_B013_black(self):
        '''单个网址删除取消功能'''
        self.Page.add_black_url('https://www.ithome.com')
        self.Page.click_save_or_delete_btn()
        self.Page.click_one_cb()
        self.Page.click_delete_btn()
        self.Page.click_popup_negative_btn()
        try:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_name').text, "未知")
        finally:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_url').text, "ithome.com")
        self.Page.click_delete_btn()
        self.Page.click_popup_positive_btn()
        self.base.is_display('id',self.Page.save_btn_loc[1])

    @ScreenAssert.decorator
    def test_url_B014_black(self):
        '''单个网址删除确定功能'''
        self.Page.add_black_url('https://testerhome.com/')
        self.Page.click_save_or_delete_btn()
        self.Page.click_one_cb()
        self.Page.click_delete_btn()
        self.Page.click_popup_positive_btn()
        try:
            self.assertIsNotNone(self.base.find_toast("操作成功",self.driver))
        finally:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_empty_tip').text, "空空哒~")

    @ScreenAssert.decorator
    def test_url_B015_black(self):
        '''验证添加黑名单添加多条正常网址功能'''
        self.Page.go_black_list()
        try:
            self.Page.input_nick_value('www.hao123.com')
            sleep(2)
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_load_more').text, "— 加载完毕，共1条数据 —")
        finally:
            try:
                self.Page.input_nick_value('www.qq.com')
                sleep(2)
                self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_load_more').text,
                                 "— 加载完毕，共2条数据 —")
            finally:
                self.Page.input_nick_value('www.baidu.com')
                sleep(2)
                self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_load_more').text,
                                 "— 加载完毕，共3条数据 —")
        self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_B016_black(self):
        '''验证输入已存在的网址功能'''
        self.Page.add_black_url('www.baidu.com')
        self.Page.input_nick_value('www.baidu.com')
        self.assertIsNotNone(self.base.find_toast("该网址已存在", self.driver))
        self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_B017_black(self):
        '''验证全选删除黑名单网址取消功能'''
        self.Page.add_black_url('www.baidu.com')
        self.Page.click_save_or_delete_btn()
        self.Page.click_all_cb()
        self.Page.click_delete_btn()
        self.Page.click_popup_negative_btn()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/btn_action').text,"完成")
        self.Page.click_delete_btn()
        self.Page.click_popup_positive_btn()
        self.base.is_display('id',self.Page.save_btn_loc[1])

    @ScreenAssert.decorator
    def test_url_B018_black(self):
        '''验证全选删除黑名单网址确定功能'''
        self.Page.add_black_url('www.baidu.com')
        self.Page.click_save_or_delete_btn()
        self.Page.click_all_cb()
        self.Page.click_delete_btn()
        self.Page.click_popup_positive_btn()
        self.assertIsNotNone(self.base.find_toast("操作成功", self.driver))
        self.assertIsNotNone(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/btn_action').is_enabled())
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_empty_tip').text,"空空哒~")

    @ScreenAssert.decorator
    def test_url_B019_black(self):
        '''验证添加多个黑名单网址，SQL对比'''
        self.Page.add_black_url('www.baidu.com')
        self.Page.input_nick_value('www.qq.com')
        self.Page.input_nick_value('http://www.sohu.com/')
        self.base.is_display('id',self.Page.save_btn_loc[1])
        try:
            self.assertEqual(self.sql.sql_url_black_white(0),[{'url_domain': 'baidu.com'}, {'url_domain': 'qq.com'}, {'url_domain': 'sohu.com'}])
        finally:
            self.Page.del_url()

    '''
    以下网址白名单测试用例
    '''
    @ScreenAssert.decorator
    def test_url_C001_white(self):
        '''验证白名单默认页面，如何截取固定坐标的图片做对比，小格雷logo空空大'''
        self.Page.go_white_list()
        self.base.is_display('id',self.Page.save_btn_loc[1])
        self.png.CreateCustomSizeNowPNG('test_url_C001_white',0,72,1080,1776)
        self.assertEqual(self.base.gerLocOld('test_url_C001_white'),self.base.getLocNow('test_url_C001_white'))

    @ScreenAssert.decorator
    def test_url_C002_white(self):
        '''验证白名单页面默认项'''
        self.Page.go_white_list()
        try:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_empty_tip').text, "空空哒~")
        finally:
            self.assertTrue(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/iv_back').is_enabled(), "error")

    @ScreenAssert.decorator
    def test_url_C003_white(self):
        '''验证添加白名单网址默认值以及取消功能'''
        self.Page.go_white_list()
        self.Page.click_add_black_btn()
        try:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/title').text, "添加后只允许孩子访问该网址")
        finally:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/ed_nick').text, "www.xxx.com")

    @ScreenAssert.decorator
    def test_url_C004_white(self):
        '''验证添加白名单网址取消功能'''
        self.Page.go_white_list()
        self.Page.click_add_black_btn()
        self.Page.click_popup_negative_btn()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_empty_tip').text, "空空哒~")

    @ScreenAssert.decorator
    def test_url_C005_white(self):
        '''验证添加白名单网址删除功能'''
        self.Page.go_white_list()
        self.Page.click_add_black_btn()
        self.Page.input_popup_nick('1111111')
        self.Page.input_popup_nick_clear()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/ed_nick').text, "www.xxx.com")

    @ScreenAssert.decorator
    def test_url_C006_white(self):
        '''验证添加非法格式白名单网址功能'''
        self.Page.go_white_list()
        try:
            self.Page.input_nick_value(' ')
            self.assertIsNotNone(self.base.find_toast("网址格式不正确",self.driver))
        finally:
            try:
                pass
                # self.Page.input_nick_value('www.baidu.co')
                # self.assertIsNotNone(self.base.find_toast("网址格式不正确",self.driver))
            finally:
                self.Page.input_nick_value('!@#$%^&*&')
                self.assertIsNotNone(self.base.find_toast("网址格式不正确", self.driver))

    @ScreenAssert.decorator
    def test_url_C007_white(self):
        '''添加淘宝网址'''
        self.Page.add_white_url('www.taobao.com')
        try:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_name').text, "淘宝")
        finally:
            try:
                self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_url').text,"taobao.com")
            finally:
                self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_load_more').text, "— 加载完毕，共1条数据 —")
        self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_C008_white(self):
        '''验证编辑淘宝网址时，淘宝的名称和网址'''
        self.Page.add_white_url('www.taobao.com')
        self.Page.click_url_value()
        try:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/ed_nick_name').text, "淘宝")
        finally:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/ed_nick').text, "taobao.com")
        self.Page.click_popup_negative_btn()
        self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_C009_white(self):
        '''验证取消编辑淘宝网址功能'''
        self.Page.add_white_url('www.taobao.com')
        self.Page.click_url_value()
        self.Page.click_popup_negative_btn()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_url').text, "taobao.com")
        self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_C010_white(self):
        '''验证编辑白名单网址输入非法格式的网址保存功能'''
        self.Page.add_white_url('www.taobao.com')
        self.Page.click_url_value()
        self.Page.input_popup_nick_name('')
        self.Page.click_popup_positive_btn()
        try:
            self.assertIsNotNone(self.base.find_toast("网址名称不能为空",self.driver))
        finally:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_url').text, "taobao.com")
        self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_C011_white(self):
        '''验证编辑白名单网址输入正常的名称保存功能'''
        self.Page.add_white_url('www.taobao.com')
        self.Page.click_url_value()
        self.Page.input_popup_nick_name('你猜我猜不猜')
        self.Page.click_popup_positive_btn()
        try:
            self.assertIsNotNone(self.base.find_toast("操作成功",self.driver))
        finally:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_name').text, "你猜我猜不猜")
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_url').text, "taobao.com")
        self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_C012_white(self):
        '''验证编辑白名单网址输入正常的名称和网址保存功能'''
        self.Page.add_white_url('www.taobao.com')
        self.Page.click_url_value()
        self.Page.input_popup_nick_name('绿网天下上海市分公司')
        self.Page.input_popup_nick_url('www.itqq.com')
        self.Page.click_popup_positive_btn()
        try:
            self.assertIsNotNone(self.base.find_toast("操作成功",self.driver))
        finally:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_name').text, "绿网天下上海市分公司")
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_url').text, "itqq.com")
        self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_C013_white(self):
        '''单个网址删除取消功能'''
        self.Page.add_white_url('www.taobao.com')
        self.Page.click_save_or_delete_btn()
        self.Page.click_one_cb()
        self.Page.click_delete_btn()
        self.Page.click_popup_negative_btn()
        try:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_name').text, "淘宝")
        finally:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_url').text, "taobao.com")
        self.Page.click_delete_btn()
        self.Page.click_popup_positive_btn()
        self.base.is_display('id',self.Page.save_btn_loc[1])

    @ScreenAssert.decorator
    def test_url_C014_white(self):
        '''单个网址删除确定功能'''
        self.Page.add_white_url('www.taobao.com')
        self.Page.click_save_or_delete_btn()
        self.Page.click_one_cb()
        self.Page.click_delete_btn()
        self.Page.click_popup_positive_btn()
        try:
            self.assertIsNotNone(self.base.find_toast("操作成功",self.driver))
        finally:
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_empty_tip').text, "空空哒~")

    @ScreenAssert.decorator
    def test_url_C015_white(self):
        '''验证添加白名单添加多条正常网址功能'''
        self.Page.go_white_list()
        try:
            self.Page.input_nick_value('www.taobao.com')
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_load_more').text, "— 加载完毕，共1条数据 —")
        finally:
            try:
                self.Page.input_nick_value('www.sohu.com')
                self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_load_more').text,
                                 "— 加载完毕，共2条数据 —")
            finally:
                self.Page.input_nick_value('www.ithome.com')
                self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_load_more').text,
                                 "— 加载完毕，共3条数据 —")
        self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_C016_white(self):
        '''验证输入已存在的网址功能'''
        self.Page.add_white_url('www.sohu.com')
        self.Page.input_nick_value('www.sohu.com')
        self.assertIsNotNone(self.base.find_toast("该网址已存在", self.driver))
        self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_C017_white(self):
        '''验证全选删除白名单网址取消功能'''
        self.Page.add_white_url('www.sohu.com')
        self.Page.click_save_or_delete_btn()
        self.Page.click_all_cb()
        self.Page.click_delete_btn()
        self.Page.click_popup_negative_btn()
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/btn_action').text,"完成")
        self.Page.click_delete_btn()
        self.Page.click_popup_positive_btn()
        self.base.is_display('id',self.Page.save_btn_loc[1])

    @ScreenAssert.decorator
    def test_url_C018_white(self):
        '''验证全选删除白名单网址确定功能'''
        self.Page.add_white_url('www.sohu.com')
        self.Page.click_save_or_delete_btn()
        self.Page.click_all_cb()
        self.Page.click_delete_btn()
        self.Page.click_popup_positive_btn()
        self.assertIsNotNone(self.base.find_toast("操作成功", self.driver))
        self.assertIsNotNone(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/btn_action').is_enabled())
        self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_empty_tip').text,"空空哒~")

    @ScreenAssert.decorator
    def test_url_C019_white(self):
        '''验证添加多个白名单网址，SQL对比'''
        self.Page.add_white_url('www.taobao.com')
        self.Page.input_nick_value('www.51.com')
        self.Page.input_nick_value('www.51job.com')
        self.base.is_display('id',self.Page.save_btn_loc[1])
        try:
            self.assertEqual(self.sql.sql_url_black_white(1),[{'url_domain': '51.com'}, {'url_domain': '51job.com'}, {'url_domain': 'taobao.com'}])
        finally:
            self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_D001_white_and_black(self):
        '''验证已存在黑名单中的网址，白名单添加提示'''
        self.Page.go_black_list()
        self.Page.input_nick_value('www.baidu.com')
        self.Page.click_white_btn()
        self.Page.input_nick_value('www.baidu.com')
        self.assertIsNotNone(self.base.find_toast("已经在黑名单中",self.driver))

    @ScreenAssert.decorator
    def test_url_D012_white_and_black(self):
        '''验证已存在白名单中的网址，黑名单添加提示'''
        self.Page.go_white_list()
        self.Page.input_nick_value('www.qq.com')
        self.Page.click_black_btn()
        self.Page.input_nick_value('www.qq.com')
        self.assertIsNotNone(self.base.find_toast("已经在白名单中",self.driver))
    '''
    关键字
    '''
    @ScreenAssert.decorator
    def test_url_E001_key(self):
        '''验证网址管理-关键字默认页面显示，截图对比'''
        self.Page.go_key()
        self.base.is_display('id',self.Page.add_key_btn[1])
        self.png.CreateCustomSizeNowPNG('test_url_E001_key',0,72,1080,1776)
        self.assertEqual(self.base.gerLocOld('test_url_E001_key'),self.base.getLocNow('test_url_E001_key'))

    @ScreenAssert.decorator
    def test_url_E002_key(self):
        '''验证网址管理-系统关键字温馨提示，截图对比'''
        self.Page.go_key()
        self.Page.click_key_switch()
        self.base.is_display('id',self.Page.popup_negative_loc[1])
        self.png.CreateCustomSizeNowPNG('test_url_E002_key',81,703,999,1148)
        self.assertEqual(self.base.gerLocOld('test_url_E002_key'),self.base.getLocNow('test_url_E002_key'))

    @ScreenAssert.decorator
    def test_url_E003_key(self):
        '''验证网址管理-系统关键字温馨提示取消功能，截图对比'''
        self.Page.go_key()
        self.Page.click_key_switch()
        sleep(1)
        self.Page.click_popup_negative_btn()
        self.png.CreateCustomSizeNowPNG('test_url_E003_key',0,72,1080,1776)
        self.assertEqual(self.base.gerLocOld('test_url_E003_key'),self.base.getLocNow('test_url_E003_key'))

    @ScreenAssert.decorator
    def test_url_E004_key(self):
        '''验证网址管理-系统关键字温馨提示确定功能，截图对比'''
        self.Page.go_key()
        self.Page.click_key_switch()
        sleep(1)
        self.Page.click_popup_positive_btn()
        self.base.is_display('id',self.Page.key_switch_btn[1])
        self.png.CreateCustomSizeNowPNG('test_url_E004_key',0,396,1080,628)
        self.assertEqual(self.base.gerLocOld('test_url_E004_key'),self.base.getLocNow('test_url_E004_key'))

    @ScreenAssert.decorator
    def test_url_E005_key(self):
        '''验证网址管理-开关系统关键字，SQL对比'''
        self.Page.go_key()
        try:
            self.assertEqual(self.sql.sql_switch_key(),{'value': '0'})
        finally:
            self.Page.click_key_switch()
            self.base.is_display('id', self.Page.key_switch_btn[1])
            self.assertEqual(self.sql.sql_switch_key(),{'value': '1'})

    @ScreenAssert.decorator
    def test_url_E006_key(self):
        '''验证网址管理-开关系统关键字，SQL对比'''
        self.Page.go_key()
        self.Page.click_add_key()
        try:
            self.assertEqual(self.base.get_assert('id',self.Page.popup_nick_loc[1]).text,'请输入关键字，例如：游戏')
        finally:
            self.assertEqual(self.driver.find_element_by_id('com.gwchina.lssw.parent:id/title').text,'拦截孩子搜索的关键字')

    @ScreenAssert.decorator
    def test_url_E007_key(self):
        '''验证网址管理添加关键字，删除关键字的值以及取消功能'''
        self.Page.go_key()
        self.Page.click_add_key()
        try:
            self.Page.input_popup_nick('测试数据')
            self.Page.input_popup_nick_clear()
            self.assertEqual(self.base.get_assert('id',self.Page.popup_nick_loc[1]).text,'请输入关键字，例如：游戏')
        finally:
            self.Page.click_popup_negative_btn()
            self.base.is_display('id', self.Page.key_switch_btn[1])
            self.png.CreateCustomSizeNowPNG('test_url_E007_key', 0, 72, 1080, 1776)
            self.assertEqual(self.base.gerLocOld('test_url_E007_key'), self.base.getLocNow('test_url_E007_key'))

    @ScreenAssert.decorator
    def test_url_E008_key(self):
        '''验证网址管理添加关键字，关键字的长度限制为4-16个字符或2-8个汉字!,toast验证'''
        self.Page.go_key()
        try:
            self.Page.input_nick_value('1')
            self.base.find_toast("关键字的长度限制为4-16个字符或2-8个汉字!",self.driver)
        finally:
            try:
                self.Page.input_nick_value('上')
                self.base.find_toast("关键字的长度限制为4-16个字符或2-8个汉字!",self.driver)
            finally:
                try:
                    self.Page.input_nick_value('qwertyuiop123456789')
                    self.base.find_toast("关键字的长度限制为4-16个字符或2-8个汉字!", self.driver)
                finally:
                    self.Page.input_nick_value('上海绿网天下分公司')
                    self.base.find_toast("关键字的长度限制为4-16个字符或2-8个汉字!", self.driver)

    @ScreenAssert.decorator
    def test_url_E009_key(self):
        '''验证网址管理正常添加关键字,toast验证操作成功'''
        self.Page.go_key()
        try:
            self.Page.input_nick_value('lolcsgo')
            self.base.find_toast("操作成功",self.driver)
        finally:
            self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_E010_key(self):
        '''验证网址管理添加重复关键字，,toast验证关键字已存在'''
        self.Page.go_key()
        self.Page.input_nick_value('lolcsgo')
        self.Page.input_nick_value('lolcsgo')
        try:
            self.base.find_toast("关键字已存在", self.driver)
        finally:
            self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_E011_key(self):
        '''验证网址管理添加空的关键字，,toast验证关键字不能为空'''
        self.Page.go_key()
        self.Page.click_add_key()
        self.Page.click_popup_positive_btn()
        self.base.find_toast("关键字不能为空!", self.driver)

    @ScreenAssert.decorator
    def test_url_E012_key(self):
        '''验证网址管理添加多个关键字，文本验证 — 加载完毕，共3条数据 —'''
        self.Page.go_key()
        try:
            self.Page.input_nick_value('测试数据1')
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_load_more').text, "— 加载完毕，共1条数据 —")
            self.Page.input_nick_value('测试数据2')
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_load_more').text, "— 加载完毕，共2条数据 —")
            self.Page.input_nick_value('测试数据3')
            self.assertEqual(self.base.get_assert('id', 'com.gwchina.lssw.parent:id/tv_load_more').text, "— 加载完毕，共3条数据 —")
        finally:
            self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_E013_key(self):
        '''验证网址管理添加多个关键字，sql验证 —'''
        self.Page.go_key()
        try:
            self.Page.input_nick_value('测试数据4')
            self.Page.input_nick_value('测试数据5')
            self.Page.input_nick_value('测试数据6')
            self.base.is_display('id', self.Page.key_switch_btn[1])
            self.assertEqual(self.sql.sql_url_key(),[{'keyword': '测试数据4'}, {'keyword': '测试数据5'}, {'keyword': '测试数据6'}])
        finally:
            self.Page.del_url()

    @ScreenAssert.decorator
    def test_url_E014_key(self):
        '''验证网址管理删除单个关键字，toast验证 —'''
        self.Page.go_key()
        self.Page.input_nick_value('测试数据7')
        self.Page.click_save_or_delete_btn()
        self.Page.click_one_cb()
        self.Page.click_delete_btn()
        self.Page.click_popup_positive_btn()
        self.base.find_toast("操作成功", self.driver)

    @ScreenAssert.decorator
    def test_url_E015_key(self):
        '''验证网址管理删除多个关键字，toast验证 —'''
        self.Page.go_key()
        self.Page.input_nick_value('测试数据8')
        self.Page.input_nick_value('测试数据9')
        self.Page.click_save_or_delete_btn()
        self.Page.click_all_cb()
        self.Page.click_delete_btn()
        self.Page.click_popup_positive_btn()
        self.base.find_toast("操作成功", self.driver)

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        log.critical("--------------------网址管理测试结束--------------------")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(URL_Management)
    unittest.TextTestRunner(verbosity=2).run(suite)
