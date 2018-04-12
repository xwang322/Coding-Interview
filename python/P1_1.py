class Solution(object):
    def twoSum(self, nums, target):
        temp = sorted(nums)
        left, right = 0, len(nums)-1
        while left < right:
            if temp[left] + temp[right] == target:
                if temp[left] != temp[right]:
                    return [nums.index(temp[left]), nums.index(temp[right])]
                else:
                    duplicate = [i for i, x in enumerate(nums) if x == temp[left]]
                    return [duplicate[0], duplicate[1]]
            elif temp[left] + temp[right] > target:
                right -= 1
            else:
                left += 1
        return []