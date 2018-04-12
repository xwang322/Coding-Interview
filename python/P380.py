class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.dictionary = {}
        

    def insert(self, val):
        if val not in self.dictionary:
            self.nums.append(val)
            self.dictionary[val] = len(self.nums)-1
            return True
        return False

    def remove(self, val):
        if val not in self.dictionary:
            return False
        else:
            index_temp = self.dictionary[val]
            element = self.nums[-1]
            self.nums[index_temp] = element
            self.dictionary[element] = index_temp
            self.nums.pop()
            del self.dictionary[val]
            return True
        

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()