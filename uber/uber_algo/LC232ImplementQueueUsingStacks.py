class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)


    def pop(self):
        if not self.stack1:
            return None
        return self.stack1.pop(0)


    def peek(self):
        if not self.stack1:
            return None
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        temp = self.stack1.pop()
        self.stack1.append(temp)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return temp


    def empty(self):
        if not self.stack1:
            return True
        return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
