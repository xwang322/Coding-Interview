'''
年纪大的三哥，在硅谷工作多年了。出了个题是只有一个院子，两个人要遛狗，两人的狗不合，所以不能同时在院子里，
这两个人各有两面旗子，只能通过举旗来通信。其实就是多线程的信号灯问题，写了代码，并walk through。最后剩下10分钟左右聊天。
'''
import threading
import time
import random
class ShareYard(object):
    def __init__(self):
        self.active = []
        self.lock = threading.Lock()

    def TakethePlace(self, name):
        with self.lock:
            self.active.append(name)
            print name + ' is in the yard'

    def LeavethePlace(self, name):
        with self.lock:
            self.active.remove(name)
            print name + ' is leaving the yard'

def worker(s, pool):
    with s:
        name = threading.currentThread().getName()
        print name
        pool.TakethePlace(name)
        time.sleep(random.random())
        pool.LeavethePlace(name)

pool = ShareYard()
s = threading.Semaphore(1)
for i in range(2):
    t = threading.Thread(target=worker, name='Dog_'+str(i), args=(s, pool))
    t.start()
