/*
* 给定一个整数数列比如-2，-1，2，3，返回代表数列的range比如-2--1，2-3
* 给出正确做法（排序+遍历），写了几个testcase
* 然后来了个followup，给出range，返回任何一个对应整数数列，遍历硬做就可以了，需要考虑一下横杠的不同情况
**/

def MergeIntToRanges(nums):
    if not nums:
        return []
    if len(nums) == 1:
        return [str(nums[0])+'-'+str(nums[0])]
    nums.sort()
    answer = []
    temp = 0
    i = 0
    while i < len(nums):
        while i < len(nums)-1 and (nums[i]+1 == nums[i+1] or nums[i] == nums[i+1]):
            i += 1
        if i == temp:
            answer.append(str(nums[i])+'-'+str(nums[i]))
            temp += 1
        else:
            answer.append(str(nums[temp])+'-'+str(nums[i]))
            temp = i+1
        i += 1
    return answer

answer = MergeIntToRanges([-2, -2, -1, -1, 0, 1, 2, 3, 5, 7])
print answer

def RangesToIntSeparate(strings):
    if not strings:
        return []
    answer = []
    for string in strings:
        length = len(string)
        for i in range(1, length-1):
            if (string[i-1].isdigit() and string[i+1].isdigit() and string[i] == '-') or (string[i] == '-' and string[i+1] == '-'):
                num1 = int(string[:i])
                num2 = int(string[i+1:])
                answer += [i for i in range(num1, num2+1)]
                break
        if '-' not in string:
            answer.append(int(string))
        if '-' == string[0] and string.count('-') == 1:
            answer.append(int(string))
    answer.sort()
    return answer

answer = RangesToIntSeparate(['-7','-2--1', '3-5', '-9', '12'])
print answer

# If you merge them together, you remove the duplicates
def MergeIntToRanges(nums):
    if not nums:
        return []
    if len(nums) == 1:
        return [str(nums[0])+'-'+str(nums[0])]
    nums.sort()
    answer = []
    temp = 0
    i = 0
    while i < len(nums):
        while i < len(nums)-1 and (nums[i]+1 == nums[i+1] or nums[i] == nums[i+1]):
            i += 1
        if i == temp:
            answer.append(str(nums[i])+'-'+str(nums[i]))
            temp += 1
        else:
            answer.append(str(nums[temp])+'-'+str(nums[i]))
            temp = i+1
        i += 1
    return answer

def RangesToIntSeparate(strings):
    if not strings:
        return []
    answer = []
    for string in strings:
        length = len(string)
        for i in range(1, length-1):
            if (string[i-1].isdigit() and string[i+1].isdigit() and string[i] == '-') or (string[i] == '-' and string[i+1] == '-'):
                num1 = int(string[:i])
                num2 = int(string[i+1:])
                answer += [i for i in range(num1, num2+1)]
                break
        if '-' not in string:
            answer.append(int(string))
        if '-' == string[0] and string.count('-') == 1:
            answer.append(int(string))
    answer.sort()
    return answer

answer = RangesToIntSeparate(MergeIntToRanges([-2, -2, -1, -1, 0, 1, 2, 3, 5, 7]))
print answer
