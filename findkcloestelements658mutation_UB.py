/*
* 题目是given a sorted list of integers as data, a target integer, and a number k, 输出离target最近的k个elements，
* 比如 data = [1, 4, 5, 66, 66, 70, 200, 300], target = 67, k = 3, return [66, 66, 70] （实际要求输出index，不过一样的）
* 我是直接binary search找最接近的，然后左右看取最近的直到取满k个元素，这样是lg(n) + k worst case.然后面试官说当k较大（接近n）的时候接近linear，
* 有没有更好的solution， 我想了想说可能在closest element左右各找k/2个元素作为估计值形成一个window，
* 然后左右slide直到找到要求的最接近的那些元素，然后其实worst case也还是linear， 面试官提示说可以把binary search 和slide的过程组合起来，
* 也就是说以binary search的方式slide（或者说jump）， 这样可以达到log(k)，其实我没有完全搞明白如何确定该slide left 还是slide right，
* 时间差不多到了就没再继续，问了他几个问题就结束了。总体感觉不乐观，找closest的时候index off by 1 的问题纠结了一会，还是不够熟练的问题，
* 正在准备的同学可以先练习一下怎么把传统binary search改写成找到最接近的元素。

* 找到最接近的以后，比如坐标m，答案肯定在m-k到m+k之间，然后比较m-k/2和m+k/2，如果m+k/2离target更近，则m-k到m-k/2可以舍弃，以后继续这样二分来比
**/
# This is LC 658 code, needs to change, output is index, not number, and use binary recursively
def findClosestElements(arr, k, target):
    if not arr:
        return arr
    left = right = mid = bisect.bisect_left(arr, target)
    if mid-k/2 >= 0:
        left = mid-k/2
    else:
        left = 0
    if mid+k/2 <= len(arr)-1:
        right = mid+k/2
    else:
        right = len(arr)-1
    answer = []
    length = 0
    search_range = k/2
    while length < k:
        if left == judgeboundary(arr, left, right, target):
            answer += [arr[i] for i in range(left, mid+1)]
            length += mid-left+1
            left -= (k-length)/2
        else:
            answer += [arr[i] for i in range(mid, right+1)]
            length += right-mid+1
            right += (k-length)/2

def judgeboundary(arr, left, right, target):
    if target-arr[left] <= arr[right]-target:
        return left
    else:
        return right




import bisect
def findClosestElements(arr, k, target):
    if not arr:
        return arr
    left = right = mid = bisect.bisect_left(arr, target)
    if mid == 0:
        return arr[:k]
    elif mid == len(arr):
        return arr[-k:]
    if mid-k/2 >= 0:
        left = mid-k/2
    else:
        left = 0
    if mid+k/2 <= len(arr)-1:
        right = mid+k/2
    else:
        right = len(arr)-1
    answer = [arr[mid]]
    length = 1
    while length < k:
        print left, right
        if left == judgeboundary(arr, left, right, target):
            answer = [arr[i] for i in range(left, mid)]+answer
            print answer
            length += mid-left
            print length
            while length > k:
                answer.append(arr[i] for i in range(left, mid)[::-1])
            left = left-1-(k-length)/2
            right = mid+1+(k-length)/2
            print left, right, length
        else:
            answer += [arr[i] for i in range(mid+1, right+1)]
            print answer
            length += right-mid
            while length > k:
                return answer[:k]
            right = right+1+(k-length)/2
            left = mid-1-length/2
            print left, right, length

def judgeboundary(arr, left, right, target):
    if target-arr[left] <= arr[right]-target:
        return left
    else:
        return right

answer = findClosestElements([1, 4, 5, 66, 66, 67, 68, 70, 200, 300], 7, 67)
print answer
