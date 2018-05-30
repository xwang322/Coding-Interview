'''
给定一个array，当中有些数字只出现一次，有些重复出现。写一个function去掉重复的数字，使得output的array保留所有出现过的数字且没有重复。要保留顺序。
例如input = [4,4,3,6,6,7,7,7]，output =[4,3,6,7]。
'''
def filterOutDuplicate(nums):
    if not nums:
        return []
    visited = set()
    answer = []
    for num in nums:
        if num not in visited:
            answer.append(num)
            visited.add(num)
    return answer

answer = filterOutDuplicate([4,4,3,6,6,7,7,7])
print answer
