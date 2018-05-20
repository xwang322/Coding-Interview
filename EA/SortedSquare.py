'''
给一个排好序的sorted array，输出排好序的square，如[-4, -2, 1, 3, 5] 输出 [1, 4, 9, 16, 25] 要求O(n)
'''
def sortedSquare(nums):
    if not nums:
        return []
    left = 0
    right = len(nums)-1
    while left < right:
        if abs(nums[left]) < abs(nums[right]):
            right -= 1
        else:
            left += 1
    middle = left
    answer = []
    answer.append(nums[middle]**2)
    left = middle - 1
    right = middle + 1
    while left >= 0 and right <= len(nums)-1:
        if abs(nums[left]) < abs(nums[right]):
            answer.append(nums[left]**2)
            left -= 1
        else:
            answer.append(nums[right]**2)
            right += 1
    if left < 0:
        while right <= len(nums)-1:
            answer.append(nums[right]**2)
            right += 1
    else:
        while left >= 0:
            answer.append(nums[left]**2)
            left -= 1
    return answer


answer = sortedSquare([-4, -2, 0, 1, 3, 5])
print answer
