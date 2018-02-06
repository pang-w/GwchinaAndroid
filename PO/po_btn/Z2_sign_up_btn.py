from selenium.webdriver.common.by import By


config = {
    'start_page_loc':(By.ID,'com.gwchina.lssw.parent:id/guidance_video'),
    'start_button_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_experience_guide'),
    #忘记密码、立即注册
    'register_btn': (By.ID, 'com.gwchina.lssw.parent:id/tv_register'),  # 登录页面注册按钮
    'input_re_username_btn': (By.ID, 'com.gwchina.lssw.parent:id/edit_username'),  # 手机号输入框
    'code_btn': (By.ID, 'com.gwchina.lssw.parent:id/btn_valid_code'),  # 验证码按钮
    'input_code_btn': (By.ID, 'com.gwchina.lssw.parent:id/edit_valid_code'),  # 验证码输入框
    'input_new_pwd_btn': (By.ID, 'com.gwchina.lssw.parent:id/ed_pwd'),  # 输入新密码
    'input_new2_pwd_btn': (By.ID, 'com.gwchina.lssw.parent:id/ed_confirm_pwd'),  # 输入重复密码
    'confirm_register_btn': (By.ID, 'com.gwchina.lssw.parent:id/btn_register'),  # 立即注册按钮
    'license_btn': (By.ID, 'com.gwchina.lssw.parent:id/tv_license'),  # 《最终用户许可协议》
    'other_register_btn': (By.ID, 'com.gwchina.lssw.parent:id/layout_right'),  # 其它注册方式
    'email_register_btn': (By.ID, 'com.gwchina.lssw.parent:id/tv_email'),  # 邮箱注册
    'account_register_btn': (By.ID, 'com.gwchina.lssw.parent:id/tv_account'),  # 账号注册
    'all_back_btn': (By.ID, 'com.gwchina.lssw.parent:id/iv_back'),  # 所有页面返回键
    'iknow_btn': (By.ID, 'com.gwchina.lssw.parent:id/btn_positive'),  # 我知道了按钮

}