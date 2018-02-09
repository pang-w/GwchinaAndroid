from public import Common
from time import sleep
from PO.po_btn import B8_feedback_btn


class config(Common.Action):

    setting_loc = B8_feedback_btn.config['setting_loc']
    feedback_loc = B8_feedback_btn.config['feedback_loc']
    title_feedback_loc = B8_feedback_btn.config['title_feedback_loc']
    submit_loc = B8_feedback_btn.config['submit_loc']
    input_feedback_loc = B8_feedback_btn.config['input_feedback_loc']
    input_contact_loc = B8_feedback_btn.config['input_contact_loc']
    qq_group_loc = B8_feedback_btn.config['qq_group_loc']
    qq_service_loc = B8_feedback_btn.config['qq_service_loc']
    feedback_dail_loc = B8_feedback_btn.config['feedback_dail_loc']

    def click_setting(self):
        sleep(8)
        self.find_element(*self.setting_loc).click()

    def click_feedback(self):
        self.find_element(*self.feedback_loc).click()

    def click_title_feedback(self):
        self.find_element(*self.title_feedback_loc).click()

    def click_submit(self):
        self.find_element(*self.submit_loc).click()

    def click_input_feedback(self,msg):
        self.find_element(*self.input_feedback_loc).send_keys(msg)

    def click_input_contact(self,email):
        self.find_element(*self.input_contact_loc).send_keys(email)

    def click_qq_group(self):
        self.find_element(*self.qq_group_loc).click()

    def click_qq_service(self):
        self.find_element(*self.qq_service_loc).click()

    def click_feedback_dail(self):
        self.find_element(*self.feedback_dail_loc).click()

    def go_feedback(self):
        self.click_setting()
        self.swipe_to_down(1.2, 10)
        self.click_feedback()
        self.is_display(self.submit_loc[1])

    def input_msg(self,feedback,contact):
        sleep(1)
        self.click_input_feedback(feedback)
        sleep(1)
        self.click_input_contact(contact)
        sleep(1)
        self.click_submit()