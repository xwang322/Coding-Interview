'''
烙印，挺不专业的，给了个LRU Cache让做题就开始玩手机，写完问了些follow up，改成thread-safe，感觉答的一般
'''
import threading
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        self.head = Node(0,0)
        self.tail = Node(float('inf'), float('inf'))
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dictionary = {}
        self.lock = threading.Lock()

    def get(self, key):
        if key in self.dictionary:
            self.lock.acquire()
            temp = self.dictionary[key]
            self._remove(temp)
            self._add(temp)
            print 'A'
            self.lock.release()
            return temp.value
        return -1

    def put(self, key, value):
        if key in self.dictionary:
            self.lock.acquire()
            self._remove(self.dictionary[key])
            new = Node(key, value)
            self._add(new)
            self.dictionary[key] = new
            print 'B'
            self.lock.release()
        else:
            new = Node(key, value)
            self.lock.acquire()
            self._add(new)
            self.dictionary[key] = new
            print 'C'
            self.lock.release()
        if len(self.dictionary) > self.capacity:
            temp = self.head.next
            self.lock.acquire()
            self._remove(temp)
            del self.dictionary[temp.key]
            self.lock.release()

    def _remove(self, node):
        p = node.prev
        q = node.next
        p.next = q
        q.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.next = self.tail
        node.prev = p
        self.tail.prev = node

def worker1(p):
    p.put(1, 3)
    p.put(2, 3)
    p.get(1)

def worker2(p):
    p.put(1,2)
    p.get(2)
    p.put(4,2)

process = LRUCache(2)
threads = []
for worker in [worker1, worker2]:
    threads.append(threading.Thread(target = worker, args = (process,)))
    threads[-1].start()
main_thread = threading.currentThread()
for thread in threads:
    if thread is not main_thread:
        thread.join()
