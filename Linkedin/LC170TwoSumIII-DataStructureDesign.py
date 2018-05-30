class TwoSum(object):

    def __init__(self):
        self.dictionary = collections.defaultdict(list)
        self.list = []

    def add(self, number):
        self.dictionary[number].append(len(self.list))
        self.list.append(number)

    def find(self, value):
        for i in self.dictionary:
            if value-i != i and value-i in self.dictionary:
                return True
            elif value-i == i and len(self.dictionary[i]) >= 2:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
