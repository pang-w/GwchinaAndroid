import time

from public import Common
from PO.po_btn import Z1_Login_btn


class LoginPage(Common.Action):

    start_page_loc =  Z1_Login_btn.config['start_page_loc']
    start_button_loc = Z1_Login_btn.config['start_button_loc']
    def click_video(self):
        self.find_element(*self.start_page_loc).click()
    def click_start(self):
        self.find_element(*self.start_button_loc).click()

    '''忘记密码、立即注册'''
    register_btn = Z1_Login_btn.config['register_btn']
    input_re_username_btn = Z1_Login_btn.config['input_re_username_btn']
    code_btn = Z1_Login_btn.config['code_btn']
    input_code_btn = Z1_Login_btn.config['input_code_btn']
    input_new_pwd_btn = Z1_Login_btn.config['input_new_pwd_btn']
    input_new2_pwd_btn = Z1_Login_btn.config['input_new2_pwd_btn']
    confirm_register_btn = Z1_Login_btn.config['confirm_register_btn']
    license_btn = Z1_Login_btn.config['license_btn']
    other_register_btn = Z1_Login_btn.config['other_register_btn']
    email_register_btn = Z1_Login_btn.config['email_register_btn']
    account_register_btn = Z1_Login_btn.config['account_register_btn']
    all_back_btn = Z1_Login_btn.config['all_back_btn']
    iknow_btn = Z1_Login_btn.config['iknow_btn']

    def click_register_btn(self):
        self.find_element(*self.register_btn).click()

    def input_re_username(self,username):
        return self.find_element(*self.input_re_username_btn).send_keys(username)

    def click_code_btn(self):
        self.find_element(*self.code_btn).click()

    def input_code(self,code):
        return self.find_element(*self.input_code_btn).send_keys(code)

    def input_new_pwd(self,code):
        return self.find_element(*self.input_new_pwd_btn).send_keys(code)

    def input_new2_pwd(self,code):
        return self.find_element(*self.input_new2_pwd_btn).send_keys(code)

    def click_confirm_register_btn(self):
        self.find_element(*self.confirm_register_btn).click()

    def click_license_btn(self):
        self.find_element(*self.license_btn).click()

    def click_other_register_btn(self):
        self.find_element(*self.other_register_btn).click()

    def click_email_register_btn(self):
        self.find_element(*self.email_register_btn).click()

    def click_account_register_btn(self):
        self.find_element(*self.account_register_btn).click()

    def click_all_back_btn(self):
        self.find_element(*self.all_back_btn).click()

    def click_iknow_btn(self):
        self.find_element(*self.iknow_btn).click()

    def go_register_page(self):
        self.click_video()
        self.click_start()
        self.click_register_btn()

    def go_mail_register_page(self):
        self.go_register_page()
        self.click_other_register_btn()
        self.click_email_register_btn()

    def go_mail_register_input(self,mail):
        self.go_register_page()
        self.click_other_register_btn()
        self.click_email_register_btn()
        self.input_re_username(mail)
        self.click_code_btn()

    def go_account_register_page(self):
        self.go_register_page()
        self.click_other_register_btn()
        self.click_account_register_btn()

    def input_account_value(self,username,pwd1,pwd2):
        time.sleep(2)
        self.input_re_username(username)
        self.input_new_pwd(pwd1)
        self.input_new2_pwd(pwd2)
        self.click_confirm_register_btn()
