class RandomizedSet(object):

    def __init__(self):
        self.stack = []
        self.dictionary = {}

    def insert(self, val):
        if val in self.dictionary:
            return False
        else:
            self.stack.append(val)
            self.dictionary[val] = len(self.stack)-1
            return True

    def remove(self, val):
        if val not in self.dictionary:
            return False
        else:
            temp = self.stack[-1]
            position = self.dictionary[val]
            self.dictionary[temp] = position
            self.stack[position] = temp
            self.stack.pop()
            self.dictionary.pop(val, 0)
            return True
        
    def getRandom(self):
        return self.stack[random.randint(0, len(self.stack)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
