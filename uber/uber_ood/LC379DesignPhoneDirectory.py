import collections
class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        self.maxnumber = maxNumbers
        self.array = collections.deque([i for i in range(maxNumbers)])
        self.used = set()

    def get(self):
        if not self.array:
            return -1
        node = self.array.popleft()
        self.used.add(node)
        return node


    def check(self, number):
        if number < 0 or number >= self.maxnumber:
            return -1
        return not number in self.used


    def release(self, number):
        if number < 0 or number >= self.maxnumber or number not in self.used:
            return -1
        self.used.remove(number)
        self.array.append(number)



# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
