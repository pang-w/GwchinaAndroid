from selenium.webdriver.common.by import By


config = {
    'start_page_loc':(By.ID,'com.gwchina.lssw.parent:id/guidance_video'),
    'start_button_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_experience_guide'),  # 孩子设备按钮
    #登录
    'username_loc': (By.ID, 'com.gwchina.lssw.parent:id/ed_username'), #点击头像按钮
    'password_loc': (By.ID, 'com.gwchina.lssw.parent:id/ed_pwd'),  # 拍摄新照片按钮
    'submit_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_login'),  # 从相册选择按钮
    'agree_loc':(By.ID,'com.gwchina.lssw.parent:id/tv_dialog_agree'), #头像取消按钮
    'qq_login_btn_loc': (By.ID, 'com.gwchina.lssw.parent:id/ib_qq'),  # 设备名称按钮
    'weixin_login_btn_loc': (By.ID, 'com.gwchina.lssw.parent:id/ib_weixin'),  # 孩子手机号码名称按钮
    'sina_login_btn_loc': (By.ID, 'com.gwchina.lssw.parent:id/ib_sina'),  # 小主性别按钮
    #忘记密码、立即注册
    'forgot_pwd_btn': (By.ID, 'com.gwchina.lssw.parent:id/tv_forget_pwd'),#小主出生年月按钮
    'register_btn': (By.ID, 'com.gwchina.lssw.parent:id/tv_register'),  # 小主年级按钮
    'input_re_username_btn': (By.ID, 'com.gwchina.lssw.parent:id/edit_username'),  # 我是孩子的 按钮
    'code_btn': (By.ID, 'com.gwchina.lssw.parent:id/btn_valid_code'),  # 删除设备按钮
    'input_code_btn': (By.ID, 'com.gwchina.lssw.parent:id/edit_valid_code'),  # 返回按钮
    'input_new_pwd_btn': (By.ID, 'com.gwchina.lssw.parent:id/ed_pwd'),  # 取消按钮
    'input_new2_pwd_btn': (By.ID, 'com.gwchina.lssw.parent:id/ed_confirm_pwd'),  # 确定按钮
    'confirm_register_btn': (By.ID, 'com.gwchina.lssw.parent:id/btn_register'),  # 删除设备密码文本框
    'license_btn': (By.ID, 'com.gwchina.lssw.parent:id/tv_license'),  # 删除设备密码取消按钮
    'other_register_btn': (By.ID, 'com.gwchina.lssw.parent:id/layout_right'),  # 删除设备密码确定按钮
    'email_register_btn': (By.ID, 'com.gwchina.lssw.parent:id/tv_email'),  # 修改出生年月、年级、孩子的--完成按钮
    'account_register_btn': (By.ID, 'com.gwchina.lssw.parent:id/tv_account'),  # 小主性别男
    'all_back_btn': (By.ID, 'com.gwchina.lssw.parent:id/iv_back'),  # 小主性别女
    'iknow_btn': (By.ID, 'com.gwchina.lssw.parent:id/btn_positive'),  # 删除设备后空的页面标题设备管理

}