'''
自己实现一个stack，可以O(1)实现push， pull， getMiddle，讨论了几分钟写完又跑了一下test。
'''
import collections
class Solution(object):
    def __init__(self):
        self.stack1 = collections.deque()
        self.stack2 = collections.deque()
        self.flag = True
        self.flag2 = True

    def push(self, x):
        if not self.flag:
            if self.stack2:
                self.stack1.append(self.stack2.popleft())
                self.stack2.append(x)
        else:
            self.stack2.append(x)
        self.flag = not self.flag

    def getMiddle(self):
        return self.stack1[-1]

    def peek(self):
        return self.stack2[-1]

    def pull(self):
        if self.flag2:
            self.flag2 = not self.flag2
            return self.stack2.pop()
        else:
            self.stack2.appendleft(self.stack1.pop())
            self.flag2 = not self.flag2
            return self.stack2.pop()

obj = Solution()
obj.push(1)
print obj.stack1
print obj.stack2
obj.push(2)
print obj.stack1
print obj.stack2
obj.push(3)
print obj.stack1
print obj.stack2
obj.push(4)
print obj.stack1
print obj.stack2
print obj.getMiddle()
print obj.pull()
print obj.stack1
print obj.stack2
print obj.getMiddle()
print obj.pull()
print obj.stack1
print obj.stack2
obj.push(7)
print obj.stack1
print obj.stack2
print obj.pull()
print obj.stack1
print obj.stack2
