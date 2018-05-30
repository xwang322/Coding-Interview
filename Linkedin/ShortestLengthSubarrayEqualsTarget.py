'''
positive int array [1,2,3,4,2,2,1]， target number 10， output the shortest length of subarray which sum up to target
'''
def findShortestLengthofSubarray(nums, target):
    if not nums:
        return []
    if target in nums:
        return 1
    start = 0
    end = 0
    answer = len(nums)+1
    if sum(nums) < target:
        return []
    temp = 0
    flag = False
    while start <= end:
        while temp < target and end < len(nums):
            if end == len(nums)-1:
                flag = True
            temp += nums[end]
            end += 1
        if temp == target:
            answer = min(answer, end-start)
        while temp > target:
            temp -= nums[start]
            start += 1
        if temp == target:
            answer = min(answer, end-start)
        if start < end:
            temp -= nums[start]
            start += 1
        if flag:
            break
    return answer

answer = findShortestLengthofSubarray([1,2,3,4,3,5,5], 10)
print answer
