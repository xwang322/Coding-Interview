'''
一串数中找missing number: example: (1, 3, 2, 2, 5) n = 5, 4 is missing, 2 is duplicate
所以要return的就是4,开始提了两种，一种是用hashmap，一种sort之后做。面试官不满意时间和空间复杂度。让我 时间O(n) 空间O(1)的方法。
这道题目好像和lc中的missing number 不一样，思路和lc中另一道题很像（First Missing Positve)
'''
def FindMissingNumber(nums):
    # O(n) time and O(1) space
    if not nums:
        return None
    length = len(nums)
    if length == 1:
        return 1 if nums[0] != 1 and nums[0] > 0 else None
    for num in nums:
        if num <= 0 or num > length:
            return None
    for i in range(length):
        if nums[i] <= length and nums[nums[i]-1] != nums[i]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
    for i in range(length):
        if nums[i] != i+1:
            return i+1
    return length

def FindMissingNumber(nums):
    # O(nlogn) time, O(1) space
    if not nums:
        return None
    length = len(nums)
    if length == 1:
        return 1 if nums[0] != 1 and nums[0] > 0 else None
    for num in nums:
        if num <= 0 or num > length:
            return None
    nums.sort()
    duplicate = 0
    for i in range(length-1):
        if nums[i] == nums[i+1]:
            duplicate = nums[i]
        elif nums[i] + 2 == nums[i+1]:
            return nums[i]+1
    return length

def FindMissingNumber(nums):
    # O(n) time, O(n) space
    if not nums:
        return None
    length = len(nums)
    if length == 1:
        return 1 if nums[0] != 1 and nums[0] > 0 else None
    for num in nums:
        if num <= 0 or num > length:
            return None
    dictionary = {}
    duplicate = 0
    for index, num in enumerate(nums):
        if num not in dictionary:
            dictionary[num] = index+1
        else:
            duplicate = num
    for value in dictionary.values():
        if value not in dictionary:
            return value

answer = FindMissingNumber([1,2,2,3,5])
print answer
