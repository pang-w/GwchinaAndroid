import requests
from public import Log

log = Log.Logger(logger='APIDataInfo').getLog()

url = 'http://ic.cs1.gwchina.cn/system/connect'
def get_token():
    try:
        host = 'http://ic.cs1.gwchina.cn'
        endpoint = '/system/connect'
        headers = {"oem_type": "LSSW", "key": "98243574", "lang": "chs", "serial_no": "sn-android-parent"}
        url = ''.join(host + endpoint)
        resp = requests.post(url=url, json=headers)
        text = resp.json()
        token_value = text['token']
        log.info("My_api -> get_token -> 获取token值 %s " % token_value)
        return token_value
    except:
        log.info("My_api -> get_token -> 获取token值失败 ")

class GetApi(object):
    host = 'http://ic.cs1.gwchina.cn'
    token = get_token()

    def login_user(self):
        try:
            endpoint = '/user/authorize/login'
            headers = {'token':GetApi.token}
            json = {"mode": 1,"oem_type": "lssw","password": "aa111111","user_name": "18521524172","soft_version":"5.9.0"}
            url = ''.join(self.host + endpoint)
            resp = requests.post(url = url,headers = headers,json = json)
            log.info("My_api -> login_user -> 默认账号18521524172 -> 登陆成功")
            return resp.json()
        except:
            log.info("My_api -> login_user -> 默认账号18521524172 -> 登陆失败")

    def get_user_id(self):
        try:
            endpoint = '/user/authorize/login'
            headers = {'token':GetApi.token}
            json = {"mode": 1,"oem_type": "lssw","password": "aa111111","user_name": "18521524172","soft_version":"5.9.0"}
            url = ''.join(self.host + endpoint)
            resp = requests.post(url = url,headers = headers,json = json)
            text = resp.json()
            user_id = text['user_id']
            log.info("My_api -> get_user_id -> 默认账号18521524172 账号的 user_id 为 %s " % user_id)
            return user_id
        except:
            log.info("My_api -> get_user_id -> 默认账号18521524172 -> 获取 user_id 失败")


    def get_bind_id(self):
        try:
            self.login_user()
            endpoint = '/device/info/query'
            headers = {'token':GetApi.token}
            json = {"user_name": "18521524172"}
            url = ''.join(self.host + endpoint)
            resp = requests.post(url = url,headers = headers,json = json)
            text = resp.json()
            list = text['list']
            list_0 = list[0]
            bind_id = list_0['bind_id']
            log.info("My_api -> get_bind_id -> 默认账号18521524172 绑定的默认设备天机MINI03 bind_id 为 %s " % bind_id)
            return bind_id
        except:
            log.info("My_api -> get_bind_id -> 默认账号18521524172 获取 bind_id 失败 ")

    def get_time(self):
        self.login_user()
        bind_id = self.get_bind_id()
        endpoint = '/time/set2/getfamily'
        headers = {'token':GetApi.token}
        json = {"bind_id":bind_id}
        url = ''.join(self.host + endpoint)
        resp = requests.post(url = url,headers = headers,json = json)
        text = resp.json()
        return text

    #未区分家或学校，默认添加一个地址
    def get_area(self):
        try:
            self.login_user()
            bind_id = self.get_bind_id()
            endpoint = '/device/setting/rail/getlist'
            headers = {'token':GetApi.token}
            json = {"bind_id":bind_id,"type":""}
            url = ''.join(self.host + endpoint)
            resp = requests.post(url = url,headers = headers,json = json)
            json_text = resp.json()
            # address = text['address']
            key_value = json_text['list']
            list_value = key_value[0]
            address = list_value['address']
            log.info("My_api -> get_area -> 默认账号18521524172 绑定的默认设备天机MINI03 -> 仅获取 list[0]")
            log.info("My_api -> get_area -> 获取安全区域地址为 %s " % address)
            return address
        except:
            log.info("My_api -> get_area -> 默认账号18521524172 绑定的默认设备天机MINI03 -> 获取安全区域失败")

if __name__ == '__main__':
    x = GetApi().login_user()
    print(x)
