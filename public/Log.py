# _*_ coding: utf-8 _*_
import logging
import os.path,sys
import time

from config import configReadInfo

abs_path = os.path.dirname(os.path.abspath('.'))

class Logger(object):

    def __init__(self, logger):
        '''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''

        logLevel = {
            1: logging.NOTSET,
            2: logging.DEBUG,
            3: logging.INFO,
            4: logging.WARNING,
            5: logging.ERROR,
            6: logging.CRITICAL
        }

        level = int(configReadInfo.ReadConfig().readConfigInfo()['LogLevel'])
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logLevel[level])

        # 创建一个handler，用于写入日志文件
        now = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        # log_path = os.path.dirname(os.getcwd()) + '/log/'  # 项目根目录下/Logs 保存日志
        log_path = abs_path + '\\log\\' + day + '\\'
        # 如果case组织结构式 /testsuit/featuremodel/xxx.py ， 那么得到的相对路径的父路径就是项目根目录
        if os.path.exists(log_path):
            log_name = os.path.join(log_path + now + '.log')
        else:
            os.mkdir(r'%s' % log_path)
            log_name = os.path.join(log_path + now + '.log')
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getLog(self):
        return self.logger

if __name__ == '__main__':
    level = int(configReadInfo.ReadConfig().readConfigInfo()['LogLevel'])

    print(level)