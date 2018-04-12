/*
* 第二题， 给list of double d1, d2, 3， 找到 list of integer 是floor 或 ceil，
* i1, i2, i3, round (sum (d1...)) = sum(i1, i2, i3) with minimum (sum (abs(d1-i1)...)， 地里的题
**/
import math
def findNearestInteger(nums):
    if not nums:
        return []
    n = len(nums)
    floor_list = list(map(lambda x: math.floor(x), nums))
    ceil_list = list(map(lambda x: math.ceil(x), nums))
    target = round(sum(nums))
    answer = 0
    candidates = []
    dfs(candidates, floor_list, ceil_list, n, [])
    temp = []
    for candidate in candidates:
        if sum(candidate) == target:
            temp.append(candidate)
    abs_list = []
    for each in temp:
        abs_list.append(sum(abs(each[i]-nums[i]) for i in range(n)))
    index = abs_list.index(min(abs_list))
    return temp[index] if temp else []

def dfs(candidates, floor_list, ceil_list, n, path):
    if len(path) == n:
        candidates.append(path)
        return
    if len(floor_list) > 0:
        dfs(candidates, floor_list[1:], ceil_list[1:], n, path+[floor_list[0]])
        dfs(candidates, floor_list[1:], ceil_list[1:], n, path+[ceil_list[0]])


answer = findNearestInteger([-1.4, 2.3, 0.9])
print answer
