from PIL import Image
from public import Log
import os

''' 待添加逻辑 判断是xpath 、 id'''
''' 创建预期结果图片，首先截取元素所在的整体页面(存放 .\data\page )，在截图元素图片(存放 .\data\loc )'''
''' 用例对比，open .\data\loc 对应的元素 与 用例所截取的图片做对比 '''

PngDataPath = os.path.dirname(os.path.abspath('.')) + '\\data'
log = Log.Logger(logger='CreatePNG').getLog()

class CreatePNG(object):

    def __init__(self,driver):
        self.driver = driver

    def CreateNowPNG(self,v,png,loc):
        self.driver.get_screenshot_as_file(PngDataPath +  '\\page\\%s_page.png' % png)
        log.info("截取当前页面图片保存至 .\data\page 目录下")
        if v == 'id':
            location = self.driver.find_element_by_id(loc).location
            size = self.driver.find_element_by_id(loc).size

            left = location['x']
            top =  location['y']
            right = location['x'] + size['width']
            bottom = location['y'] + size['height']

            now = Image.open(PngDataPath +  '\\page\\%s_page.png' % png)
            im = now.crop((left, top, right, bottom))
            im.save(PngDataPath +  '\\loc_now\\%s_page.png' % png)
            log.info("截取页面元素图片保存至 .\data\loc_now 目录下")

        elif v == 'xpath':
            location = self.driver.find_element_by_xpath(loc).location
            size = self.driver.find_element_by_xpath(loc).size

            left = location['x']
            top =  location['y']
            right = location['x'] + size['width']
            bottom = location['y'] + size['height']

            now = Image.open(PngDataPath +  '\\page\\%s_page.png' % png)
            im = now.crop((left, top, right, bottom))
            im.save(PngDataPath +  '\\loc_now\\%s_page.png' % png)

    '''
    self.png.CreateCustomSizeOldPNG('time_A5',0,548,1080,1273)
    适配 1080 1920 分辨率，例如天机迷你
    '''
    #获取自定义大小的图片做对比
    def CreateCustomSizeOldPNG(self,png,start_x,start_y,end_x,end_y):
        self.driver.get_screenshot_as_file(PngDataPath +  '\\page\\%s_page.png' % png)
        box = (start_x, start_y, end_x, end_y)
        image = Image.open(PngDataPath +  '\\page\\%s_page.png' % png)
        newImage = image.crop(box)
        newImage.save(PngDataPath +  '\\loc_old\\%s.png' % png)

    def CreateCustomSizeNowPNG(self,png,start_x,start_y,end_x,end_y):
        from time import sleep
        sleep(2)
        self.driver.get_screenshot_as_file(PngDataPath +  '\\page\\%s_page.png' % png)
        box = (start_x, start_y, end_x, end_y)
        image = Image.open(PngDataPath +  '\\page\\%s_page.png' % png)
        newImage = image.crop(box)
        newImage.save(PngDataPath +  '\\loc_now\\%s.png' % png)
        # log.info("截取页面自定义大小 %s.png 图片保存至 .\data\loc_now 目录下" % png)
        log.info("Save the custom size screen snapshot as the ‘.\data\loc_now’ folder. png : %s " % png)

if __name__ == '__main__':
    png = 1
    print(PngDataPath +  '\\page\\%s_page.png' % png)