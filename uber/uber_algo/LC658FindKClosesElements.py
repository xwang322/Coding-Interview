/*
* 第二轮 国人小哥放水。 给个数组 一个target， 找k个离这个数组最近的数， 用双指针秒了。
**/

class Solution(object):
    def findClosestElements(self, arr, k, x):
        left = right = bisect.bisect_left(arr, x)
        while right-left < k:
            if left == 0:
                return arr[:k]
            if right == len(arr):
                return arr[-k:]
            if x-arr[left-1] <= arr[right]-x:
                left -= 1
            else:
                right += 1
        return arr[left:right]
