from selenium.webdriver.common.by import By


config = {
    'setting_loc':(By.ID,'com.gwchina.lssw.parent:id/rb_settings'),
    'account_loc': (By.XPATH, '//android.widget.TextView[@text="账号与安全"]'),
    'logout_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_logout'), #退出登录按钮
    'phone_loc': (By.XPATH, '//android.widget.TextView[@text="绑定手机"]'),  # 绑定手机按钮

    'phone_negative_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_negative'),  # 开关弹窗取消按钮
    'phone_positive_loc':(By.ID,'com.gwchina.lssw.parent:id/btn_positive'), #开关弹窗确定按钮
    'phone_input_loc': (By.ID, 'com.gwchina.lssw.parent:id/ed_nick'),  # 开关弹窗输入按钮
    'phone_pwd_error_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_dialog_confirm'),  # 密码错误确认按钮

    'pattern_switch_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_switch_pwd'),  # 图案密码锁开关
    'pattern_negative_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_negative'),#开关弹窗取消按钮
    'pattern_positive_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_positive'),  # 开关弹窗确定按钮
    'pattern_input_loc': (By.ID, 'com.gwchina.lssw.parent:id/ed_nick'),  # 开关弹窗输入按钮
    'pattern_pwd_error_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_dialog_confirm'),  # 密码错误确认按钮
    'logout_negative_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_negative'),  # 退出登录取消按钮
    'logout_positive_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_positive'),  # 退出登录确定按钮
    'change_pwd_loc': (By.XPATH, '//android.widget.TextView[@text="修改密码"]'),  # 修改密码按钮
    'change_old_pwd_loc': (By.ID, 'com.gwchina.lssw.parent:id/edit_old_pwd'),  # 旧密码输入框
    'change_new_pwd_loc': (By.ID, 'com.gwchina.lssw.parent:id/edit_new_pwd'),  # 新密码输入框
    'change_new_pwd_sec_loc': (By.ID, 'com.gwchina.lssw.parent:id/edit_new_pwd_sec'),  # 新密码重复输入框
    'change_pwd_confirm_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_modify_confirm'),  #修改密码确认按钮
    'forget_pwd_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_action'),  # 忘记密码按钮
    'all_back_loc': (By.ID, 'com.gwchina.lssw.parent:id/iv_back'),  # 所有页面的返回按钮

    'pwd_error_text':(By.ID,'com.gwchina.lssw.parent:id/tv_dialog_tip')

}