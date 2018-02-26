__author__ = 'Never deter till tomorrow that which you can do today. _20180131'
# -*- coding: utf-8 -*-
import os,math,subprocess
from testDAL import adbCommon

device = adbCommon.AndroidDebugBridge().attachedDevices()

#获取手机版本，型号，品牌，设备名
def getPhoneInfo(devices):
    cmd = "adb -s " + devices + " shell cat /system/build.prop "
    phone_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.readlines()

    phone_list = {}
    release = "ro.build.version.release=" # 版本
    model = "ro.product.model=" #型号
    brand = "ro.product.brand=" # 品牌
    device = "ro.product.device=" # 设备名
    try:
        for line in phone_info:
            for i in line.split():
                temp = i.decode()
                if temp.find(release) >= 0:
                    phone_list["release"] = temp[len(release):]
                    break
                if temp.find(model) >= 0 :
                    phone_list["model"] = temp[len(model):]
                    break
                if temp.find(brand) >= 0 :
                    phone_list["brand"] = temp[len(brand):]
                    break
                if temp.find(device) >= 0 :
                    phone_list["device"] = temp[len(device):]
                    break
        return phone_list
    except:
        print('1')

#获得手机运行最大内存
#os.popen() 方法用于从一个命令打开一个管道。
def getMaxRunMemory(devices):
    cmd = "adb -s " + devices + " shell cat /proc/meminfo"
    get_cmd = os.popen(cmd).readlines()
    max_memory = 0
    max_memory_str = "MemTotal"
    for line in get_cmd:
        if line.find(max_memory_str) >= 0 :
            max_memory = line[len(max_memory_str) + 1:].replace("kB", "").strip()
            break
    return int(max_memory)

# 得到几核cpu
def getCpuInfo(devices):
    cmd = "adb -s " +devices +" shell cat /proc/cpuinfo"
    get_cmd = os.popen(cmd).readlines()
    find_str = "processor"
    int_cpu = 0
    for line in get_cmd:
        if line.find(find_str) >= 0:
            int_cpu += 1
    return str(int_cpu) + "核"

# 得到手机分辨率
def getPhonePix(devices):
    result = os.popen("adb -s " + devices+ " shell wm size", "r")
    return result.readline().split("Physical size:")[1]

#未调试
def get_avg_raw(l_men, devices):
    '''

    :param l_men: 内存使用列表
    :param devices: 设备名
    :return:
    '''
    l_men = [math.ceil(((l_men[i])/getMaxRunMemory(devices))*1024) for i in range(len(l_men))]  # 获取每次占用内存多少
    if len(l_men) > 0 :
            return str(math.ceil(sum(l_men)/len(l_men))) + "%"
    return "0%"

if __name__ == '__main__':
    from testDAL import adbCommon

    device = adbCommon.AndroidDebugBridge().attachedDevices()
    # device1 = list(adbCommon.AndroidDebugBridge().attachedDevices())
    # print(device1)
    # for i in device:
    #     print(i)
    # devices = device[1]
    # print(devices)

    print(getPhoneInfo(device)['release'])
    # print(getMaxRunMemory('83d7d437'))
    # print(getCpuInfo('83d7d437'))
    # print(getPhonePix('83d7d437'))
    # print(get_avg_raw('83d7d437'))