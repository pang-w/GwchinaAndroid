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

    '''登录'''
    username_loc = Z1_Login_btn.config['username_loc']
    password_loc = Z1_Login_btn.config['password_loc']
    submit_loc = Z1_Login_btn.config['submit_loc']
    agree_loc = Z1_Login_btn.config['agree_loc']
    qq_login_btn_loc = Z1_Login_btn.config['qq_login_btn_loc']
    weixin_login_btn_loc = Z1_Login_btn.config['weixin_login_btn_loc']
    sina_login_btn_loc = Z1_Login_btn.config['sina_login_btn_loc']

    def input_username(self,username):
        self.driver.find_element(*self.username_loc).send_keys(username)

    def input_password(self,password):
        self.driver.find_element(*self.password_loc).send_keys(password)

    def click_submit(self):
        self.find_element(*self.submit_loc).click()

    def click_agree(self):
        self.find_element(*self.agree_loc).click()

    def click_qq_btn(self):
        self.find_element(*self.qq_login_btn_loc).click()

    def click_wx_btn(self):
        self.find_element(*self.weixin_login_btn_loc).click()

    def click_sina_btn(self):
        self.find_element(*self.sina_login_btn_loc).click()

    def login(self,username1,password1):
        self.click_video()
        self.click_start()
        time.sleep(2)
        self.input_username(username1)
        self.input_password(password1)
        self.click_submit()

    def login_page(self,username,password):
        self.input_username(username)
        self.input_password(password)
        self.click_submit()

    def click_point(self,x,y):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        piont_x = width / x
        piont_y = height / y
        #1080 1776
        self.driver.tap([(piont_x,piont_y)],500)

    def qq_login(self):
        self.click_video()
        self.click_start()
        self.click_qq_btn()
        time.sleep(15)
        self.click_point(2,1.2)
        # self.driver.tap([(540, 1475)], 500)

    def wx_login(self):
        self.click_video()
        self.click_start()
        self.click_wx_btn()
        time.sleep(15)
        self.click_point(2,1.5)
        # self.driver.tap([(529, 1184)], 500)

    def sina_login(self):
        self.click_video()
        self.click_start()
        self.click_sina_btn()
        time.sleep(15)
        self.click_point(2,1.95)
        # self.driver.tap([(520, 910)], 500)