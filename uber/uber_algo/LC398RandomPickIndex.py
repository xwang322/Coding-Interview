class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        i = 0
        count = 0
        answer = -1
        while i < len(self.nums):
            if self.nums[i] == target:
                count += 1
                if random.randint(0, count-1) == 0:
                    answer = i
            i += 1
        return answer

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
