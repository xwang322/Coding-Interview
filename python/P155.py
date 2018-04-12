class MinStack(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)
        if len(self.stack2)==0 or x<= self.stack2[-1]:
            self.stack2.append(x)

    def pop(self):
        top = self.stack1.pop()
        if top == self.stack2[-1]:
            self.stack2.pop()

    def top(self):
        return self.stack1[-1]
        
    def getMin(self):
        return self.stack2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()