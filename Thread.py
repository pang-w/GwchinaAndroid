# -*- coding: utf-8 -*-

import threading
from time import sleep,ctime

def music(file,time):
    for i in range(time):
        print('play to %s! %s ' % (file,ctime()))
        sleep(2)

def movie(file,time):
    for i in range(time):
        print('play to %s! %s ' % (file,ctime()))
        sleep(2)

threads = []
t1 = threading.Thread(target=music,args=("音乐",2))
threads.append(t1)

t2 = threading.Thread(target=movie,args=("电影",3))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("allend %s" % ctime())



    # music("nihao",2)
    # movie("大世界",2)
    # print("allend %s" % ctime())
# for i in range(2):
#     x = "你好"
#     print('play to %s! %s ' %(x,ctime()))
#     sleep(2)