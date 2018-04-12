'''
怎么实现一个系统，如果key不在里面就新加一个entry并返回true，如果key在里面就直接返回false，类似unix系统里的touch这个命令。
先讲了单机版的，主要focus在write lock怎么整
'''
import threading

class Touch(object):
    def __init__(self):
        self.array = set()
        self.lock = threading.Lock()

    def _add(self, key):
        if key in self.array:
            self.lock.acquire()
            print 'A'
            self.lock.release()
            return False
        else:
            self.lock.acquire()
            self.array.add(key)
            print 'B'
            self.lock.release()
            return True

    def _delete(self, key):
        if key not in self.array:
            self.lock.acquire()
            print 'C'
            self.lock.release()
            return False
        else:
            self.lock.acquire()
            self.array.remove(key)
            print 'D'
            self.lock.release()
            return True

def worker1(p):
    p._add(1)
    p._add(2)
    p._add(4)

def worker2(p):
    p._add(1)
    p._add(4)
    p._add(2)

process = Touch()
threads = []
for worker in [worker1, worker2]:
    threads.append(threading.Thread(target = worker, args = (process,)))
    threads[-1].start()
main_thread = threading.currentThread()
for thread in threads:
    if thread is not main_thread:
        thread.join()
