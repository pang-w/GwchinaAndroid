from selenium.webdriver.common.by import By


config = {
    'setting_loc':(By.ID,'com.gwchina.lssw.parent:id/rb_settings'),
    'feedback_loc': (By.XPATH, '//android.widget.TextView[@text="意见反馈"]'),  # 关于我们按钮
    'title_feedback_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_title'), #名称
    'submit_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_action'),  # 提交
    'input_feedback_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_content'),  # 输入内容
    'input_contact_loc':(By.ID,'com.gwchina.lssw.parent:id/tv_content_way'), #联系方式
    'qq_group_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_feed_back_qq_group'),  # 官方QQ
    'qq_service_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_feed_back_qq'),  # 客服QQ
    'feedback_dail_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_feed_back_dail'),  # 反馈专线
}