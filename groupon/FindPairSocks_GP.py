/*
* 第一轮：给了不同号码的袜子，让你匹配到一双之后就输出，剩下未匹配到的最后输出。比如，1，3，2，1，1，2，4 输出：1，2，3，1，4. set做就可以
**/
def FindPairSocks(array):
    set1 = set()
    set2 = set()
    answer = []
    for num in array:
        if num in set1:
            set2.add(num)
            set1.remove(num)
        else:
            set1.add(num)
    for num in set2:
        answer.append(num)
    for num in set1:
        answer.append(num)
    return answer

answer = FindPairSocks([1,3,2,1,1,1,2,4,4])
print answer
