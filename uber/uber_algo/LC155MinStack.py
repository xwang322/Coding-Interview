class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        currmin = self.getMin()
        if x < currmin or currmin == None:
            currmin = x
        self.stack.append([x, currmin])

    def pop(self):
        self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][0]

    def getMin(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
