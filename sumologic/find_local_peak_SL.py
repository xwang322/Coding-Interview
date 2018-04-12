/*
* find local peak
* Find any one peak element from an unsorted array.pick element is an element having previous and next items bigger.
**/

def findLocalPeak(nums):
    return nums[search(nums, 0, len(nums)-1)]

def search(nums, start, end):
    if start == end:
        return start
    if start + 1 == end:
        return start if nums[start]>nums[end] else end
    mid = (start+end)/2
    if nums[mid] < nums[mid-1]:
        return search(nums, start, mid-1)
    if nums[mid] < nums[mid+1]:
        return search(nums, mid+1, end)
    return mid


answer = findLocalPeak([1,2,3,1])
print answer
