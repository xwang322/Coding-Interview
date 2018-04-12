/*
* 利口 幺儿吧，一个一个处理，找到第一个长度为M的连续数列
**/
def longestConsecutive(nums, m):
    if not nums:
        return []
    dictionary = {}
    for num in nums:
        start = end = num
        if num in dictionary:
            continue
        if num-1 not in dictionary and num+1 not in dictionary:
            dictionary[num] = (start, end)
        if num+1 in dictionary:
            end = dictionary[num+1][1]
        if num-1 in dictionary:
            start = dictionary[num-1][0]
        dictionary[start] = dictionary[end] = dictionary[num] = (start, end)
        if end-start+1 == m:
            return [i for i in range(start, end+1)]
    return []

answer = longestConsecutive([100, 1, 3, 200, 2, 4], 3)
print answer
