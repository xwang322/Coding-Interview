/*
* 12.1 第二轮电面，国人，uber eats。信号不大好，对面就说中文了。
* 在CodePair上写代码，原题是给你一个排序的序列，然你找出target在序列中出现了多少次。对面是Java的，然后我就说C++的库函数中可以直接调用上下限的二分。
* 他就要求手工实现lower_bound和upper_bound，秒切。
* 然后聊了一下他的业务。
**/
# use Python built-in function first
import bisect
def findHowManyTimesOccurance(nums, target):
    if not nums:
        return 0
    return bisect.bisect(nums, target) - bisect.bisect_left(nums, target)

answer = findHowManyTimesOccurance([5,7,7,8,8,10], 8)
print answer

# use two pointer method
def findHowManyTimesOccurance(nums, target):
    if not nums:
        return 0
    left = findFirstPosition(nums, target)
    right = findLastPosition(nums, target)
    return right-left

answer = findHowManyTimesOccurance([0,3,5,5,5,5,5,7,8,8,9,10],0)
print answer

def findFirstPosition(nums, target):
    l, r = 0, len(nums)-1
    while l < r:
        mid = (l+r)/2
        if nums[mid] == target:
            if nums[mid-1] != target:
                return mid
            else:
                r = mid-1
        elif nums[mid] > target:
            r = mid-1
        else:
            l = mid+1
    if nums[l] < target:
        return l+1
    return l

# answer = findFirstPosition([0,3,7,8,8,10],0)
# print answer

def findLastPosition(nums, target):
    l, r = 0, len(nums)-1
    while l < r:
        mid = (l+r)/2
        if nums[mid] == target:
            if nums[mid+1] != target:
                return mid+1
            else:
                l = mid+1
        elif nums[mid] > target:
            r = mid-1
        else:
            l = mid+1
    if target >= nums[l]:
        return l+1
    return l

# answer = findLastPosition([0,3,7,10],0)
# print answer
