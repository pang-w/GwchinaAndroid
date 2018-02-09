from public import Common
from time import sleep
from PO.po_btn import B3_childdevice_btn


class child_device(Common.Action):

    setting_loc = B3_childdevice_btn.config['setting_loc']
    device_loc = B3_childdevice_btn.config['device_loc']
    head_title_loc = B3_childdevice_btn.config['head_title_loc']
    camera_loc = B3_childdevice_btn.config['camera_loc']
    photo_loc = B3_childdevice_btn.config['photo_loc']
    head_cancel_loc = B3_childdevice_btn.config['head_cancel_loc']
    device_title_loc = B3_childdevice_btn.config['device_title_loc']
    device_phone_loc = B3_childdevice_btn.config['device_phone_loc']
    child_sex_loc = B3_childdevice_btn.config['child_sex_loc']
    child_birth_loc = B3_childdevice_btn.config['child_birth_loc']
    child_grade_loc = B3_childdevice_btn.config['child_grade_loc']
    child_guardian_loc = B3_childdevice_btn.config['child_guardian_loc']
    delete_btn_loc = B3_childdevice_btn.config['delete_btn_loc']
    back_btn_loc = B3_childdevice_btn.config['back_btn_loc']
    negative_btn_loc = B3_childdevice_btn.config['negative_btn_loc']
    positive_btn_loc = B3_childdevice_btn.config['positive_btn_loc']
    inpout_text_loc = B3_childdevice_btn.config['inpout_text_loc']
    pwd_negative_btn_loc = B3_childdevice_btn.config['pwd_negative_btn_loc']
    pwd_positive_btn_loc = B3_childdevice_btn.config['pwd_positive_btn_loc']
    finish_btn_loc = B3_childdevice_btn.config['finish_btn_loc']
    boy_btn_loc = B3_childdevice_btn.config['boy_btn_loc']
    girl_btn_loc = B3_childdevice_btn.config['girl_btn_loc']
    null_device_loc = B3_childdevice_btn.config['null_device_loc']

    def click_setting(self):
        sleep(8)
        self.find_element(*self.setting_loc).click()

    def click_device(self):
        self.find_element(*self.device_loc).click()

    def click_head_title(self):
        self.find_element(*self.head_title_loc).click()

    def click_camera(self):
        self.find_element(*self.camera_loc).click()

    def click_head_cancel(self):
        self.find_element(*self.head_cancel_loc).click()

    def click_device_title(self):
        self.find_element(*self.device_title_loc).click()

    def click_child_phone(self):
        self.find_element(*self.device_phone_loc).click()

    def click_child_sex(self):
        self.find_element(*self.child_sex_loc).click()

    def click_child_birth_(self):
        self.find_element(*self.child_birth_loc).click()

    def click_child_grade(self):
        self.find_element(*self.child_grade_loc).click()

    def click_child_guardian(self):
        self.find_element(*self.child_guardian_loc).click()

    def click_delete_btn(self):
        self.find_element(*self.delete_btn_loc).click()

    def click_back_btn(self):
        self.find_element(*self.back_btn_loc).click()

    def click_negative_btn(self):
        self.find_element(*self.negative_btn_loc).click()

    def click_positive_btn(self):
        self.find_element(*self.positive_btn_loc).click()

    def input_text_btn(self,password):
        self.find_element(*self.inpout_text_loc).send_keys(password)

    def click_pwd_negative_btn(self):
        self.find_element(*self.pwd_negative_btn_loc).click()

    def click_pwd_positive_btn(self):
        self.find_element(*self.pwd_positive_btn_loc).click()

    def click_finish_btn(self):
        self.find_element(*self.finish_btn_loc).click()

    def click_boy_btn(self):
        self.find_element(*self.boy_btn_loc).click()

    def click_girl_btn(self):
        self.find_element(*self.girl_btn_loc).click()

    def go_child_device(self):
        self.click_setting()
        self.click_device()
        self.is_display(self.null_device_loc[1])


    def swipe_to_child_down(self,start_x,start_y,end_x,end_y):  #分辨率适用于天机MINI（锁定菜单栏）
        # 下滑屏幕
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / start_x , height / start_y , width / end_x , height / end_y , 1000)
        sleep(1)

    def swipe_one_grade_down(self):
        self.swipe_to_down(2,4)
        sleep(1)
        self.click_child_grade()
        sleep(1)
        self.swipe_to_child_down(1.96, 1.41, 1.96, 1.568)
        sleep(1)
        self.click_finish_btn()

    def swipe_one_birth_down(self):
        self.swipe_to_down(2,4)
        self.click_child_birth_()
        sleep(1)
        self.swipe_to_child_down(3.6, 1.366, 3.6, 1.558)
        sleep(1)
        self.swipe_to_child_down(1.35, 1.366, 1.35, 1.558)
        sleep(1)
        self.click_finish_btn()

    def swipe_one_guardian_down(self):
        self.swipe_to_down(2, 4)
        self.click_child_guardian()
        sleep(1)
        self.swipe_to_child_down(1.93, 1.316, 1.93, 1.423)
        sleep(1)
        self.click_finish_btn()

    def check_child_phone(self,input_text):
        self.click_child_phone()
        self.input_text_btn(input_text)
        self.click_positive_btn()

