from selenium.webdriver.common.by import By
'''
弃用
元素直接写入page内
'''

config = {
    'time_btn_loc': (By.XPATH, '//android.widget.TextView[@text="时间管理"]'),  #时间管理
    'Guide_home_page_btn':(By.ID,'com.gwchina.lssw.parent:id/iv_time_guide'),  # 引导主页面
    'more_btn':(By.ID,'com.gwchina.lssw.parent:id/tv_more'),
    'Guide_confirm_page_btn': (By.ID, 'com.gwchina.lssw.parent:id/tv_confirm'), #引导页我知道了按钮
    'save_btn':(By.ID,'com.gwchina.lssw.parent:id/btn_action'), #保存按钮
    'save_negative_btn': (By.ID, 'com.gwchina.lssw.parent:id/btn_negative'),  # 保存取消按钮
    'save_positive_btn': (By.ID, 'com.gwchina.lssw.parent:id/btn_positive'),  # 保存确定按钮

    'back_btn':(By.ID,'com.gwchina.lssw.parent:id/iv_back'), #返回按钮
    'time_1_btn': (By.XPATH, '//android.widget.TextView[@text="一"]'),  # 周几按钮
    'time_2_btn': (By.XPATH, '//android.widget.TextView[@text="二"]'),  # 周几按钮
    'time_3_btn': (By.XPATH, '//android.widget.TextView[@text="三"]'),  # 周几按钮
    'time_4_btn': (By.XPATH, '//android.widget.TextView[@text="四"]'),  # 周几按钮
    'time_5_btn': (By.XPATH, '//android.widget.TextView[@text="五"]'),  # 周几按钮
    'time_6_btn': (By.XPATH, '//android.widget.TextView[@text="六"]'),  # 周几按钮
    'time_7_btn': (By.XPATH, '//android.widget.TextView[@text="日"]'),  # 周几按钮
}