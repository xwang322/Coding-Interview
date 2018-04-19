'''
判断一个字符串里没有重复字符
'''
import collections
def JudgeDuplicates(string):
    counter = collections.Counter(string)
    if any(each > 1 for each in counter.values()):
        return False
    return True

answer = JudgeDuplicates('abb')
print answer
