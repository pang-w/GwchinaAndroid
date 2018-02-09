import configparser,os

class ReadConfig(object):

    def __init__(self):
        self.configPath = os.path.dirname(os.path.abspath('.')) + '\\config\\configInfo.ini'
        self.config = configparser.ConfigParser()
        self.config.read(self.configPath)
        self.configLogDict = {'LogLevel':''}
        self.configDeviceDict = {'port':'','platformName':''}

    def readConfigInfo(self):
        self.configLogDict['LogLevel'] = self.config.get('LogLevel','logLevel')
        return self.configLogDict

    def readDeviceInfo(self):
        self.configDeviceDict['port'] = self.config.get('device','port')
        self.configDeviceDict['platformName'] = self.config.get('device','platformName')
        return self.configDeviceDict


if __name__ == '__main__':
    print(ReadConfig().readConfigInfo()['LogLevel'])
    print(ReadConfig().readDeviceInfo()['port'])
    print(ReadConfig().readDeviceInfo()['platformName'])