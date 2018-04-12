'''
第一道题：给定“UBERCAB"这个string，然后给另外一个string， 求需要多少个”UBERCAB"这样的单词，才能组成输出的单词，
比如”bear car“，那么久输出2，如果是“Amazon”，那么就输出-1，应该“UBERCAB"里面没有”Z"
'''
import collections
def countHowMany(s, t):
    if not s and not t:
        return 1
    elif not s:
        return -1
    elif not t:
        return 0
    else:
        counter_s = collections.Counter(s)
        counter_t = collections.Counter(''.join(t.strip().split()))
        for each in counter_t.keys():
            if each not in counter_s.keys():
                return -1
        temp = {}
        for each in counter_s.keys():
            if each not in counter_t.keys():
                temp[each] = 1
            else:
                temp[each] = int(counter_t[each]/counter_s[each]) + (counter_t[each]%counter_s[each]>0)
        return max(temp.values())


answer = countHowMany('ubercab','bear car')
print answer
