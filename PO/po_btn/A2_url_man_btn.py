from selenium.webdriver.common.by import By

'''
弃用
元素直接写入page内
'''

config = {
    'url_btn_loc':(By.XPATH,'//android.widget.TextView[@text="网址管理"]'),
    'back_btn_loc': (By.ID, 'com.gwchina.lssw.parent:id/iv_back'),  # 关于我们按钮
    'save_btn_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_action'), #格雷盒子 名称
    'rank_btn_loc': (By.XPATH, '//android.widget.TextView[@text="管理等级"]'),  # 当前版本5.9.4
    'expand_btn_loc': (By.ID, 'com.gwchina.lssw.parent:id/iv_expand'),  # 检测版本
    'level_btn_loc':(By.ID,'com.gwchina.lssw.parent:id/tv_hint'), #版本说明
    'level_low_btn_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_level_low'),  # 邮箱联系
    'level_middle_btn_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_level_middle'),  # 邮箱联系的值support@gwchina.cn
    'level_high_btn_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_level_high'),  # 邮箱联系的值support@gwchina.cn

    'popup_nick_loc': (By.ID, 'com.gwchina.lssw.parent:id/ed_nick'),
    'popup_negative_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_negative'),  # 关于我们按钮
    'popup_positive_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_positive'),  # 格雷盒子 名称
    'one_cb_loc': (By.ID, 'com.gwchina.lssw.parent:id/cb'),  # 当前版本5.9.4
    'all_cb_loc': (By.ID, 'com.gwchina.lssw.parent:id/cb_selectall'),  # 检测版本
    'delete_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_delete'),  # 版本说明
    'url_value_loc': (By.ID, 'com.gwchina.lssw.parent:id/tv_url'),  # 邮箱联系
    'url_popup_nick_name': (By.ID, 'com.gwchina.lssw.parent:id/ed_nick_name'),  # 邮箱联系的值support@gwchina.cn
    'url_popup_nick_url':(By.ID,'com.gwchina.lssw.parent:id/ed_nick'),
    'black_btn_loc': (By.XPATH, '//android.widget.TextView[@text="黑名单"]'),  # 邮箱联系的值support@gwchina.cn
    'add_black_and_white_btn_loc': (By.ID, 'com.gwchina.lssw.parent:id/btn_add'),  # 版本说明
    'white_btn_loc': (By.XPATH, '//android.widget.TextView[@text="白名单"]'),  # 邮箱联系
    'find_no_child_btn': (By.ID, 'com.gwchina.lssw.parent:id/message'),  # 邮箱联系
    'homepage_child_head_btn': (By.ID, 'com.gwchina.lssw.parent:id/tv_child_nick'),  # 邮箱联系的值support@gwchina.cn

    'key_btn': (By.XPATH,'//android.widget.TextView[@text="关键字"]'),
    'key_switch_btn': (By.ID, 'com.gwchina.lssw.parent:id/btn_switch'),
    'add_key_btn': (By.ID, 'com.gwchina.lssw.parent:id/btn_add'),


}