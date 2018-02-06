__author__ = 'Never deter till tomorrow that which you can do today. _20180131'

import os
import threading
import urllib.request
from urllib.error import URLError
from multiprocessing import Process

Path = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class appiumServer(object):

    def __init__(self, list_devices):
        self.list_devices = list_devices

    def startServer(self):
        for i in range(0, len(self.list_devices["appium"])):
            thread_1 = RunServer(self.list_devices["appium"][i]["config"])
            p = Process(target=thread_1.start())
            p.start()

    def stopServer(self):
        os.system('taskkill /f /im  node.exe')

    def restartServer(self):
        self.stopServer()
        self.startServer()

    def isRunning(self):
        response = None
        for i in range(0, len(self.list_devices["appium"])):
            url = " http://127.0.0.1:"+str(self.list_devices["appium"][i]["port"])+"/wd/hub"+"/status"
            try:
                response = urllib.request.urlopen(url, timeout=5)

                if str(response.getcode()).startswith("2"):
                    return True
                else:
                    return False
            except URLError:
                return False
            finally:
                if response:
                    response.close()

class RunServer(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd
    def run(self):
        os.system(self.cmd)

if __name__ == '__main__':
    import os
    from Phone import getYamlData

    list_devices = os.path.dirname(os.path.abspath('.')) + '\\Phone\\devices.yaml'
    oo = appiumServer(getYamlData.getYaml(list_devices))
    # oo.startServer()
    # print("strart server")
    # print("running server")
    oo.stopServer()
    print("stop server")