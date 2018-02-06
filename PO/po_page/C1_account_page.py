from public import Common
from time import sleep
from PO.po_btn import C1_account_btn

class AccountPage(Common.Action):

    setting_loc = C1_account_btn.config['setting_loc']
    account_loc = C1_account_btn.config['account_loc']
    logout_loc = C1_account_btn.config['logout_loc']
    phone_loc = C1_account_btn.config['phone_loc']
    phone_negative_loc = C1_account_btn.config['phone_negative_loc']
    phone_positive_loc = C1_account_btn.config['phone_positive_loc']
    phone_input_loc = C1_account_btn.config['phone_input_loc']
    phone_pwd_error_loc = C1_account_btn.config['phone_pwd_error_loc']
    pattern_switch_loc = C1_account_btn.config['pattern_switch_loc']
    pattern_negative_loc = C1_account_btn.config['pattern_negative_loc']
    pattern_positive_loc = C1_account_btn.config['pattern_positive_loc']
    pattern_input_loc = C1_account_btn.config['pattern_input_loc']
    pattern_pwd_error_loc = C1_account_btn.config['pattern_pwd_error_loc']
    logout_negative_loc = C1_account_btn.config['logout_negative_loc']
    logout_positive_loc = C1_account_btn.config['logout_positive_loc']
    change_pwd_loc = C1_account_btn.config['change_pwd_loc']
    change_old_pwd_loc = C1_account_btn.config['change_old_pwd_loc']
    change_new_pwd_loc = C1_account_btn.config['change_new_pwd_loc']
    change_new_pwd_sec_loc = C1_account_btn.config['change_new_pwd_sec_loc']
    change_pwd_confirm_loc = C1_account_btn.config['change_pwd_confirm_loc']
    forget_pwd_loc = C1_account_btn.config['forget_pwd_loc']
    all_back_loc = C1_account_btn.config['all_back_loc']
    pwd_error_text = C1_account_btn.config['pwd_error_text']


    def click_setting(self):
        sleep(5)
        self.find_element(*self.setting_loc).click()

    def click_account(self):
        self.find_element(*self.account_loc).click()

    def click_logout(self):
        self.find_element(*self.logout_loc).click()

    def click_phone(self):
        self.find_element(*self.phone_loc).click()

    def click_phone_negative(self):
        self.find_element(*self.phone_negative_loc).click()

    def click_phone_positive(self):
        self.find_element(*self.phone_positive_loc).click()

    def input_phone(self,password):
        sleep(1)
        self.driver.find_element(*self.phone_input_loc).send_keys(password)

    def click_phone_pwd_error(self):
        self.find_element(*self.phone_pwd_error_loc).click()

    def go_phone(self):
        self.click_setting()
        self.click_account()
        self.click_phone()

    def check_phone_pwd(self,password):
        self.click_phone_pwd_error()
        self.click_phone()
        self.input_phone(password)
        self.click_phone_positive()

    def click_pattern_switch(self):
        self.find_element(*self.pattern_switch_loc).click()

    def click_pattern_negative(self):
        self.find_element(*self.pattern_negative_loc).click()

    def click_pattern_positive(self):
        self.find_element(*self.pattern_positive_loc).click()

    def input_pattern(self,password):
        sleep(1)
        self.driver.find_element(*self.pattern_input_loc).send_keys(password)

    def click_pattern_pwd_error(self):
        self.find_element(*self.pattern_pwd_error_loc).click()

    def go_pattern(self):
        self.click_setting()
        self.click_account()
        self.click_pattern_switch()

    def check_pattern_pwd(self,password):
        self.click_pattern_pwd_error()
        self.click_pattern_switch()
        self.input_pattern(password)
        self.click_pattern_positive()

    def click_logout_negative(self):
        self.find_element(*self.logout_negative_loc).click()

    def click_logout_positive(self):
        self.find_element(*self.logout_positive_loc).click()

    def check_logout(self):
        self.click_setting()
        self.click_account()
        self.click_logout()

    def click_change_pwd(self):
        self.find_element(*self.change_pwd_loc).click()

    def input_old_pwd(self,password):
        sleep(1)
        self.find_element(*self.change_old_pwd_loc).send_keys(password)

    def input_new_pwd(self,password):
        sleep(1)
        self.find_element(*self.change_new_pwd_loc).send_keys(password)

    def input_new_pwd_sec(self,password):
        sleep(1)
        self.find_element(*self.change_new_pwd_sec_loc).send_keys(password)

    def click_change_pwd_confirm(self):
        self.find_element(*self.change_pwd_confirm_loc).click()

    def click_forget_pwd(self):
        self.find_element(*self.forget_pwd_loc).click()

    def click_all_back(self):
        self.find_element(*self.all_back_loc).click()

    def get_pwd_error_text(self):
        return self.find_element(*self.pwd_error_text).text

    def go_change_pwd(self):
        self.click_setting()
        self.click_account()
        self.click_change_pwd()

    def check_change_pwd(self,old_pwd,new_pwd,sec_pwd):
        self.input_old_pwd(old_pwd)
        self.input_new_pwd(new_pwd)
        self.input_new_pwd_sec(sec_pwd)
        self.click_change_pwd_confirm()