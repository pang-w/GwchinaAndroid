from public import Common
from time import sleep
from PO.po_btn import B9_about_us_btn

class About_us(Common.Action):

    setting_loc = B9_about_us_btn.config['setting_loc']
    about_us_loc = B9_about_us_btn.config['about_us_loc']
    default_about_title_loc = B9_about_us_btn.config['default_about_title_loc']
    default_version_loc = B9_about_us_btn.config['default_version_loc']
    check_version_loc = B9_about_us_btn.config['check_version_loc']
    version_loc = B9_about_us_btn.config['version_loc']
    i_know_btn = B9_about_us_btn.config['i_know_btn']
    email_contact_loc = B9_about_us_btn.config['email_contact_loc']
    email_value_loc = B9_about_us_btn.config['email_value_loc']
    hotline_loc = B9_about_us_btn.config['hotline_loc']
    mzsm_loc = B9_about_us_btn.config['mzsm_loc']
    qq_loc = B9_about_us_btn.config['qq_loc']
    qq_value_loc = B9_about_us_btn.config['qq_value_loc']
    companyname_loc = B9_about_us_btn.config['companyname_loc']
    copyright_loc = B9_about_us_btn.config['copyright_loc']
    version_positive_loc = B9_about_us_btn.config['version_positive_loc']
    version_content_loc = B9_about_us_btn.config['version_content_loc']
    mzsm_value_loc = B9_about_us_btn.config['mzsm_value_loc']
    agreement_loc = B9_about_us_btn.config['agreement_loc']
    agreement_title_loc = B9_about_us_btn.config['agreement_title_loc']
    http_value_loc = B9_about_us_btn.config['http_value_loc']
    phont_negative_loc = B9_about_us_btn.config['phont_negative_loc']
    back_btn = B9_about_us_btn.config['back_btn']

    def click_setting(self):
        sleep(5)
        self.find_element(*self.setting_loc).click()
    def click_about_us(self):
        self.find_element(*self.about_us_loc).click()
    def click_default_about_title(self):
        self.find_element(*self.default_about_title_loc).click()
    def click_default_version(self):
        self.find_element(*self.default_version_loc).click()
    def click_check_version(self):
        self.is_display_loc(self.check_version_loc)
        self.find_element(*self.check_version_loc).click()
    def click_version(self):
        self.find_element(*self.version_loc).click()
    def click_i_know(self):
        self.find_element(*self.i_know_btn).click()
    def click_email_contact(self):
        self.find_element(*self.email_contact_loc).click()
    def click_email_value(self):
        self.find_element(*self.email_value_loc).click()
    def click_hotline(self):
        self.find_element(*self.hotline_loc).click()
    def click_mzsm(self):
        self.find_element(*self.mzsm_loc).click()
    def click_qq(self):
        self.find_element(*self.qq_loc).click()
    def click_qq_value(self):
        self.find_element(*self.qq_value_loc).click()
    def click_companyname(self):
        self.find_element(*self.companyname_loc).click()
    def click_copyright(self):
        self.find_element(*self.copyright_loc).click()
    def click_version_positive(self):
        self.find_element(*self.version_positive_loc).click()
    def click_version_content(self):
        self.find_element(*self.version_content_loc).click()
    def click_declare_value(self):
        self.find_element(*self.mzsm_value_loc).click()
    def click_agreement(self):
        self.find_element(*self.agreement_loc).click()
    def click_agreement_title(self):
        self.find_element(*self.agreement_title_loc).click()
    def click_http_value(self):
        self.find_element(*self.http_value_loc).click()
    def click_phone_negative(self):
        self.find_element(*self.phont_negative_loc).click()
    def click_back(self):
        self.find_element(*self.back_btn).click()
    def go_about_us(self):
        self.click_setting()
        self.swipe_to_down(1.2, 10)
        self.click_about_us()
        self.is_display_loc(self.version_loc)


