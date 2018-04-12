class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append((x, x))
        else:
            tempmin = self.stack[-1][1]
            if x < tempmin:
                self.stack.append((x, x))
            else:
                self.stack.append((x, tempmin))

    def pop(self):
        return self.stack.pop()

    def top(self):
        if not self.stack:
            return None
        else:
            return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]
