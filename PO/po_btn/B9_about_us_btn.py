from selenium.webdriver.common.by import By


config = {
    'setting_loc':(By.ID,'com.gwchina.lssw.parent:id/rb_settings'),
    'about_us_loc': (By.XPATH, '//android.widget.TextView[@text="关于我们"]'),  # 关于我们按钮
    'default_about_title_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_about_title'), #格雷盒子 名称
    'default_version_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_version_code'),  # 当前版本5.9.4
    'check_version_loc': (By.XPATH, '//android.widget.TextView[@text="检测版本"]'),  # 检测版本
    'version_loc':(By.XPATH,'//android.widget.TextView[@text="版本说明"]'), #版本说明
    'i_know_btn':(By.ID, 'com.gwchina.lssw.parent:id/btn_positive'),
    'email_contact_loc': (By.XPATH, '//android.widget.TextView[@text="邮箱联系"]'),  # 邮箱联系
    'email_value_loc': (By.XPATH, '//android.widget.TextView[@text="support@gwchina.cn"]'),  # 邮箱联系的值support@gwchina.cn
    'hotline_loc':(By.XPATH,'//android.widget.TextView[@text="服务热线"]'), # 服务热线
    'mzsm_loc': (By.XPATH, '//android.widget.TextView[@text="免责声明"]'),#免责声明
    'qq_loc': (By.XPATH, '//android.widget.TextView[@text="加入官方QQ群"]'),# 加入官方QQ群按钮
    'qq_value_loc':(By.XPATH,'//android.widget.TextView[@text="304019136"]'),#QQ群号按钮（304019136）
    'companyname_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_companyname'),#绿网天下（福建）网络科技股份有限公司
    'copyright_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_copyright'),#闽ICP备09010660号
    'version_positive_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_positive'),#版本说明 - 我知道了
    'version_content_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_content'),#版本说明 - 文本框  （目前的值[]）
    'mzsm_value_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_duty_declare'),#免责声明内容
    'agreement_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_user_agreement'),#《最终用户许可协议》
    'agreement_title_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_title'),#用户许可页面标题（《最终用户许可协议》）
    'http_value_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_http'),  # 服务网站地址
    'phont_negative_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_negative'),  # 服务热线取消
    'back_btn':(By.ID, 'com.gwchina.lssw.parent:id/iv_back'),
}
