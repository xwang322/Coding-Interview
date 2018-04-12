class MyStack(object):

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        self.queue1.append(x)

    def pop(self):
        if not self.queue1:
            return False
        while len(self.queue1)>1:
            self.queue2.append(self.queue1.pop(0))
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))
        return self.queue1.pop(0)

    def top(self):
        return self.queue1[-1]

    def empty(self):
        if not self.queue1:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
