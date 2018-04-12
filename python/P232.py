class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.top = None

    def push(self, x):
        self.stack1.append(x)
        if len(self.stack1) == 1:
            self.top = x

    def pop(self):
        while len(self.stack1)>1:
            self.stack2.append(self.stack1.pop())
        return_val = self.stack1.pop()
        while len(self.stack2)>0:
            if len(self.stack1) == 0:
                self.top = self.stack2.pop()
                self.stack1.append(self.top)
            else:
                self.stack1.append(self.stack2.pop())   
        return return_val
        

    def peek(self):
        return self.top
        
    def empty(self):
        return len(self.stack1)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()