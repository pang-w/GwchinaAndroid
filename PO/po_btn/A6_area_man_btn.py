from selenium.webdriver.common.by import By

'''
安全区域页面按钮
'''

config = {
    #主页面按钮
    'area_btn':(By.XPATH,'//android.widget.TextView[@text="安全区域"]'),
    'back_btn':(By.ID,'com.gwchina.lssw.parent:id/iv_back'),
    'save_or_edit_btn':(By.ID,'com.gwchina.lssw.parent:id/btn_action'),
    'set_area_btn':(By.ID,'com.gwchina.lssw.parent:id/tv_itemClick'),
    'add_area_btn': (By.ID, 'com.gwchina.lssw.parent:id/btn_add_fence'),
    'home_btn': (By.XPATH,'//android.widget.TextView[@text="家"]'),
    'school_btn': (By.XPATH, '//android.widget.TextView[@text="学校"]'),
    'test_btn': (By.XPATH, '//android.widget.TextView[@text="测试"]'),
    'title_btn': (By.ID, 'com.gwchina.lssw.parent:id/tv_fence_title'),#安全区域主页面生成的名称
    'address_btn':(By.ID,'com.gwchina.lssw.parent:id/tv_fence_address'), #安全区域主页面生成的地址
    'fence_time':(By.ID,'com.gwchina.lssw.parent:id/tv_fence_time'), #安全区域主页面生成的时间按钮的值 默认00：00-23:59
    'fence_rate':(By.ID,'com.gwchina.lssw.parent:id/tv_fence_rate'), #安全区域主页面生成的频率按钮的值 默认 每天
    'def_btn': (By.ID, 'com.gwchina.lssw.parent:id/ib_del'),
    'negative_btn':(By.ID,'com.gwchina.lssw.parent:id/btn_negative'),
    'positive_btn':(By.ID,'com.gwchina.lssw.parent:id/btn_positive'),
    #设置安全区域页面按钮
    'rb_position_btn':(By.ID,'com.gwchina.lssw.parent:id/rb_position'),
    'rb_time_btn': (By.ID, 'com.gwchina.lssw.parent:id/rb_time'),
    'rb_radius_btn': (By.ID, 'com.gwchina.lssw.parent:id/rb_radius'),
    'input_areaname':(By.ID,'com.gwchina.lssw.parent:id/ed_nick'),
    #设置安全区域页面
    'rb_start_end_time_btn':(By.ID,'com.gwchina.lssw.parent:id/tv_start_end_time'),
    'rb_locate_frequency_btn': (By.ID, 'com.gwchina.lssw.parent:id/tv_locate_frequency'),
    #设置时间页面
    'rb_time_range_btn':(By.ID,'com.gwchina.lssw.parent:id/tv_time_range'),
    'rb_everyday_btn':(By.ID,'com.gwchina.lssw.parent:id/rb_everyday'),
    'rb_workday_btn': (By.ID, 'com.gwchina.lssw.parent:id/rb_workday'),
    'rb_weekend_btn': (By.ID, 'com.gwchina.lssw.parent:id/rb_weekend'),

    'rb_finish_btn': (By.ID, 'com.gwchina.lssw.parent:id/btn_finish'),  #点开修改起止时间范围的完成按钮

    'rb_radius_num':(By.ID,'com.gwchina.lssw.parent:id/tv_bottom_radius_num') #点击区域范围后，当前设置的区域范围值的按钮

}
