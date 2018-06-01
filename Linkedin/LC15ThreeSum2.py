class Solution(object):
    # this version will TLE but it is more easier to understand
    def threeSum(self, nums):
        if not nums:
            return []
        nums.sort()
        answer = []
        i = 0
        while i < len(nums)-2:
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[i]+nums[j]+nums[k] == 0:
                    answer.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                    while j < k and nums[k+1] == nums[k]:
                            k -= 1
                elif nums[i]+nums[j]+nums[k] > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
        final = []
        for each in answer:
            if each not in final:
                final.append(each)
        return final
