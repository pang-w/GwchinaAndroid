from selenium.webdriver.common.by import By


config = {
    'setting_loc':(By.ID,'com.gwchina.lssw.parent:id/rb_settings'),
    'device_loc': (By.XPATH, '//android.widget.TextView[@text="孩子设备"]'),  # 孩子设备按钮
    'head_title_loc': (By.ID, 'com.gwchina.lssw.parent:id/layout_device_detail_avatar'), #点击头像按钮
    'camera_loc': (By.XPATH, '//android.widget.TextView[@text="拍摄新照片"]'),  # 拍摄新照片按钮
    'photo_loc': (By.XPATH, '//android.widget.TextView[@text="从相册选择"]'),  # 从相册选择按钮

    'head_cancel_loc':(By.ID,'com.gwchina.lssw.parent:id/tv_cancel'), #头像取消按钮
    'device_title_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_device_title'),  # 设备名称按钮
    'device_phone_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_device_phone'),  # 孩子手机号码名称按钮
    'child_sex_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_child_sex'),  # 小主性别按钮
    'child_birth_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_child_birth'),#小主出生年月按钮
    'child_grade_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_child_grade'),  # 小主年级按钮
    'child_guardian_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_child_guardian'),  # 我是孩子的 按钮
    'delete_btn_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_delete'),  # 删除设备按钮
    'back_btn_loc': (By.ID, 'com.gwchina.lssw.parent:id/iv_back'),  # 返回按钮
    'negative_btn_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_negative'),  # 取消按钮
    'positive_btn_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_positive'),  # 确定按钮
    'inpout_text_loc': (By.ID, 'com.gwchina.lssw.parent:id/ed_nick'),  # 删除设备密码文本框
    'pwd_negative_btn_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_negative'),  # 删除设备密码取消按钮
    'pwd_positive_btn_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_positive'),  # 删除设备密码确定按钮
    'finish_btn_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_finish'),  # 修改出生年月、年级、孩子的--完成按钮
    'boy_btn_loc': (By.ID, 'com.gwchina.lssw.parent:id/img_sex_boy'),  # 小主性别男
    'girl_btn_loc': (By.ID, 'com.gwchina.lssw.parent:id/img_sex_girl'),  # 小主性别女
    'null_device_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_title'),  # 删除设备后空的页面标题设备管理

}