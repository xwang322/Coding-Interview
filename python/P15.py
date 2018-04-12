class Solution(object):
    def threeSum(self, nums):
        if not nums or len(nums) == 0 or len(nums) == 1 or len(nums) == 2:
            return []
        start = 0
        answer = []
        nums.sort()
        while start <= len(nums)-3:
            if start == 0 or nums[start-1] != nums[start]:
                i = start + 1
                j = len(nums)-1
                while i < j:
                    if nums[i] + nums[j] == -nums[start]:
                        answer.append([nums[start], nums[i], nums[j]])
                        i += 1
                        j -= 1
                        while i < j and nums[i] == nums[i-1]:
                            i += 1
                        while i < j and nums[j] == nums[j+1]:
                            j -= 1
                    elif nums[i] + nums[j] > -nums[start]:
                        j -= 1
                    else:
                        i += 1
            start += 1
        return answer
                         