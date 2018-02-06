__author__ = 'Never deter till tomorrow that which you can do today. _20180131'
# -*- coding: utf-8 -*-
import os

class AndroidDebugBridge(object):

    def call_adb(self, command):
        command_result = ''
        command_test = 'adb %s ' % command
        results = os.popen(command_test, "r")
        while 1:
            line = results.readline()
            if not line: break
            command_result += line
        results.close()
        return command_result

    #检查设备
    #partition() 方法用来根据指定的分隔符将字符串进行分割。
    def attachedDevices(self):
        result = str(self.call_adb("devices"))
        devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')
        # flag = [device for device in devices if len(device) > 2]
        # print(flag)
        # if flag:
        #     return True
        # else:
        #     return False
        return devices[0]

    # 状态
    def getState(self):
        result = self.call_adb("get-state")
        result = result.strip(' \t\n\r')
        return result or None

    # 打开指定app
    def openApp(self,package_name,activity):
        result = self.call_adb("shell am start -n %s/%s" % (package_name, activity))
        check = result.partition('\n')[2].replace('\n', '').split('\t ')
        if check[0].find("Error") >= 1:
            return False
        else:
            return True

    # 根据包名得到进程id
    def getAppPid(self,pkg_name):
        # string = self.call_adb("shell ps | grep "+pkg_name)\
        #使用 \ 转义字符 adb shell  之后的内容要用引号引起来，这样就不会报这个错误了。
        string = self.call_adb(("shell \"ps | grep %s \"" ) % pkg_name)
        print(self.call_adb('devices'))
        # print(string)
        if string == '':
            return "the process doesn't exist."
        result = string.split(" ")
        # print(result[4])
        return result[4]


if __name__ == '__main__':
    print(AndroidDebugBridge().attachedDevices())
    # print(AndroidDebugBridge().getState())
    # print(AndroidDebugBridge().getAppPid(pkg_name='com.gwchina.lssw.parent'))
    # print(AndroidDebugBridge().openApp(package_name='com.gwchina.lssw.parent',activity='com.gwchina.tylw.parent.StartEntryActivity'))
    # print(AndroidDebugBridge().openApp(package_name='cn.ibona.t1_beta',activity='cn.ibona.t1.main.ui.activity.SplashActivity'))