/*
* 2/9 一面 two sum变种 给一个vector<int>和一个target 求所有相减等于target的pair数
**/
def twoSumMutation(nums, target):
    if not nums or len(nums) < 2:
        return []
    dictionary = {}
    answer = []
    for index, num in enumerate(nums):
        if num-target in dictionary or num+target in dictionary:
            if num-target in dictionary:
                answer.append([dictionary[num-target], index])
            else:
                answer.append([dictionary[num+target], index])
        dictionary[num] = index
    return answer

answer = twoSumMutation([3, 7, 11, 15], 4)
print answer
