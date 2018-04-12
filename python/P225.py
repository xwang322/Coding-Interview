class MyStack(object):
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        self.topx = None

    def push(self, x):
        self.queue1.insert(0, x)
        self.topx = x

    def pop(self):
        while len(self.queue1) > 1:
            self.topx = self.queue1.pop()
            self.queue2.insert(0, self.topx)
        return_val = self.queue1.pop()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return return_val
    
    def top(self):
        return self.topx

    def empty(self):
        return not self.queue1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()