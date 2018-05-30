class MaxStack(object):

    def __init__(self):
        self.heap = []
        self.stack = []

    def push(self, x):
        node = [-x, -len(self.stack)]
        heapq.heappush(self.heap, node)
        self.stack.append(node)

    def pop(self):
        clean(self.heap, self.stack)
        node = self.stack.pop()
        node[1] = float('-inf')
        return -node[0]

    def top(self):
        clean(self.heap, self.stack)
        return -self.stack[-1][0]

    def peekMax(self):
        clean(self.heap, self.stack)
        return -self.heap[0][0]

    def popMax(self):
        clean(self.heap, self.stack)
        node = heapq.heappop(self.heap)
        node[1] = float('-inf')
        return -node[0]

def clean(heap, stack):
    while stack[-1][1] == float('-inf'):
        stack.pop()
    while heap[0][1] == float('-inf'):
        heapq.heappop(heap)


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
