'''
第一轮 给一个很大的数组，还有一个数组是 blacklist, 要求在大数组中return 不在blacklist 里的数with equal probabity.
只能用O(blacklist)空间
'''
import random
import collections
def ReturnEqualProbability(blacklist, largelist):
    length = len(blacklist)
    answer = []
    total = 0
    for num in largelist:
        if num not in blacklist:
            total += 1
            if len(answer) < length:
                answer.append(num)
            else:
                temp = random.randint(0, total-1)
                if 0<=temp<=length-1:
                    answer[temp] = num
            print answer[random.randint(0, len(answer)-1)]

ReturnEqualProbability([2,3], [1,4,5,2,3,5,1,3,5])                
