class TwoSum(object):

    def __init__(self):
        self.list = []

    def add(self, number):
        if not self.list:
            self.list.append(number)
        else:
            index = bisect.bisect_left(self.list, number)
            self.list.insert(index, number)


    def find(self, value):
        left = 0
        right = len(self.list)-1
        while left < right:
            if self.list[left] + self.list[right] == value:
                return True
            elif self.list[left] + self.list[right] > value:
                right -= 1
            else:
                left += 1
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
