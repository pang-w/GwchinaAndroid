import configparser,os

class ReadConfig(object):

    def __init__(self):
        self.configPath = os.path.dirname(os.path.abspath('.')) + '\\config\\configInfo.ini'
        self.config = configparser.ConfigParser()
        self.config.read(self.configPath)
        self.configLogDict = {'LogLevel':''}

    def readConfigInfo(self):
        self.configLogDict['LogLevel'] = self.config.get('LogLevel','logLevel')
        return self.configLogDict


if __name__ == '__main__':
    print(ReadConfig().readConfigInfo()['LogLevel'])