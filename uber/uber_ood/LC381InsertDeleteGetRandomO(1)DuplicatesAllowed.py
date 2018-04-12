class RandomizedCollection(object):

    def __init__(self):
        self.array = []
        self.dictionary = collections.defaultdict(set)

    def insert(self, val):
        self.array.append(val)
        self.dictionary[val].add(len(self.array)-1)
        return len(self.dictionary[val]) == 1

    def remove(self, val):
        # this method will not clear a set if the key has been removed from the dictionary
        if self.dictionary[val]:
            index = self.dictionary[val].pop()
            element = self.array[-1]
            self.array[index] = element
            if self.dictionary[element]:
                self.dictionary[element].add(index)
                self.dictionary[element].discard(len(self.array)-1)
            self.array.pop()
            return True
        return False

    def getRandom(self):
        return self.array[random.randint(0, len(self.array)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
