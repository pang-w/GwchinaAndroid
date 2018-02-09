from PO.po_btn import A6_area_man_btn
from public import Common,Log
from time import sleep
from selenium.webdriver.common.by import By

'''
安全区域页面
'''

log = Log.Logger(logger='time_page').getLog()

class AreaPage(Common.Action):
    def area_point(self,piont_x,piont_y):
        sleep(5)
        self.driver.tap([(piont_x,piont_y)],500)
        sleep(5)
    #主页面按钮
    area_btn = A6_area_man_btn.config['area_btn']
    back_btn = A6_area_man_btn.config['back_btn']
    save_or_edit_btn = A6_area_man_btn.config['save_or_edit_btn']
    set_area_btn = A6_area_man_btn.config['set_area_btn']
    add_area_btn = A6_area_man_btn.config['add_area_btn']
    home_btn = A6_area_man_btn.config['home_btn']
    school_btn = A6_area_man_btn.config['school_btn']
    test_btn = A6_area_man_btn.config['test_btn']
    title_btn = A6_area_man_btn.config['title_btn']#安全区域主页面生成的名称
    address_btn = A6_area_man_btn.config['address_btn']#安全区域主页面生成的地址
    fence_time = A6_area_man_btn.config['fence_time']#安全区域主页面生成的时间按钮的值 默认00：00-23:59
    fence_rate = A6_area_man_btn.config['fence_rate']#安全区域主页面生成的频率按钮的值 默认 每天
    def_btn = A6_area_man_btn.config['def_btn']
    negative_btn = A6_area_man_btn.config['negative_btn']
    positive_btn = A6_area_man_btn.config['positive_btn']
    def click_area(self):
        self.find_element(*self.area_btn).click()
    def click_back(self):
        self.find_element(*self.back_btn).click()
        sleep(1)
    def click_save_or_edit(self):
        sleep(2)
        self.find_element(*self.save_or_edit_btn).click()
    def click_set_area(self):
        self.find_element(*self.set_area_btn).click()
    def click_add_area(self):
        self.find_element(*self.add_area_btn).click()
    def click_home(self):
        self.find_element(*self.home_btn).click()
    def click_test(self):
        self.find_element(*self.test_btn).click()
    def click_school(self):
        self.find_element(*self.school_btn).click()
    def title_text(self):
        return self.find_element(*self.title_btn).text
    def address_text(self):
        return self.find_element(*self.address_btn).text
    def fence_time_text(self):
        return self.find_element(*self.fence_time).text
    def fence_rate_text(self):
        return self.find_element(*self.fence_rate).text
    def click_def(self):
        self.find_element(*self.def_btn).click()
    def click_negative(self):
        self.find_element(*self.negative_btn).click()
    def click_positive(self):
        self.find_element(*self.positive_btn).click()


    #设置安全区域页面按钮
    rb_position_btn = A6_area_man_btn.config['rb_position_btn']
    rb_time_btn = A6_area_man_btn.config['rb_time_btn']
    rb_radius_btn = A6_area_man_btn.config['rb_radius_btn']
    input_areaname = A6_area_man_btn.config['input_areaname']

    rb_start_end_time_btn = A6_area_man_btn.config['rb_start_end_time_btn']
    rb_locate_frequency_btn = A6_area_man_btn.config['rb_locate_frequency_btn']

    def click_rb_position(self):
        self.find_element(*self.rb_position_btn).click()
    def click_rb_time(self):
        self.find_element(*self.rb_time_btn).click()
    def click_rb_radius(self):
        self.find_element(*self.rb_radius_btn).click()
    def input_area_name(self,value):
        self.find_element(*self.input_areaname).send_keys(value)
    def click_rb_start_end_time(self):
        self.find_element(*self.rb_start_end_time_btn).click()
    def click_rb_locate_frequency(self):
        self.find_element(*self.rb_locate_frequency_btn).click()

    #设置时间页面
    rb_time_range_btn = A6_area_man_btn.config['rb_time_range_btn']
    rb_everyday_btn = A6_area_man_btn.config['rb_everyday_btn']
    rb_workday_btn = A6_area_man_btn.config['rb_workday_btn']
    rb_weekend_btn = A6_area_man_btn.config['rb_weekend_btn']
    rb_finish_btn = A6_area_man_btn.config['rb_finish_btn'] #点开修改起止时间范围的完成按钮
    rb_radius_num = A6_area_man_btn.config['rb_radius_num'] #点击区域范围后，当前设置的区域范围值的按钮
    def click_rb_time_range(self):
        self.find_element(*self.rb_time_range_btn).click()
    def click_rb_everyday(self):
        self.find_element(*self.rb_everyday_btn).click()
    def click_rb_workday(self):
        self.find_element(*self.rb_workday_btn).click()
    def click_rb_weekend(self):
        self.find_element(*self.rb_weekend_btn).click()
    def click_rb_finish(self):
        self.find_element(*self.rb_finish_btn).click()
    def rb_radius_num_text(self):
        return self.find_element(*self.rb_radius_num).text

    homepage_child_head_btn = (By.ID, 'com.gwchina.lssw.parent:id/tv_child_nick')#主页上孩子头像按钮（如果存在=刷新出设备）

    def go_area_homepage(self):
        sleep(8)
        self.is_display(self.homepage_child_head_btn[1])
        self.click_area()
        # loc = self.is_display_loc(self.add_area_btn)
        # time = 1
        # while loc == False and time <= 5:
        #     log.info('A2_url_man_test（go_url_homepage）未刷新出孩子设备，第 %s 次重试' % time)
        #     print('A2_url_man_test（go_url_homepage）未刷新出孩子设备，第 %s 次重试' % time)
        #     sleep(1)
        #     self.click_negative()
        #     sleep(5)
        #     self.click_area()
        #     time += 1
        #     loc = self.is_display_loc(self.add_area_btn)
        #     if time > 5:
        #         log.info('A2_url_man_test（go_url_homepage）尝试刷新5次孩子设备，未刷新出孩子设备，多数为网络原因')
        #         print('A2_url_man_test（go_url_homepage）尝试刷新5次孩子设备，未刷新出孩子设备，多数为网络原因')
        #         break

    '''
    以下为优化的流程
    '''
    def go_rb_time_page(self):
        self.go_area_homepage()
        self.click_home()
        self.click_rb_time()

if __name__ == '__main__':
    print(AreaPage.add_area_btn[1])