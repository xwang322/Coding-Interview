'''
一个说话声音很轻没精打采的烙印，一副我欠他钱的样子，给一个list的set，{{a,b,c},{d},{e,f}}，
输出它们的Cartesian product {a,d,e},{a,d,f},{b,d,e},{b,d,f},{c,d,e},{c,d,f}，
recursive做好后要用iterative的for循环来写
'''
def cartesianProduct(lists):
    if not lists:
        return []
    for list in lists:
        if len(list) == 0:
            return []
    answer = []
    n = len(lists)
    dfs(answer, lists, n, [])
    final = []
    for each in answer:
        final.append(set(each))
    return final

def dfs(answer, lists, length, path):
    if len(path) == length:
        answer.append(path)
        return
    for index, item in enumerate(lists[0]):
        dfs(answer, lists[1:], length, path+[item])

set1 = set(['a','b','c'])
set2 = set(['d'])
set3 = set(['e','f'])
answer = cartesianProduct([set1, set2, set3])
print answer


# using iteration
def cartesianProduct(lists):
    if not lists:
        return []
    for list in lists:
        if len(list) == 0:
            return []
    answer = []
    n = len(lists)
    for i in range(n):
        if i == 0:
            temp = [[] for j in range(len(lists[i]))]
            for index, each in enumerate(lists[i]):
                temp[index] = [each]
        else:
            m = len(temp)
            current = len(lists[i])
            tmp = [[] for j in range(m*current)]
            for j in range(m*current):
                tmp[j] = temp[j%m][:]
            templist = [each for each in lists[i]]
            for j in range(m*current):
                tmp[j].append(templist[j/m])
            temp = tmp
    answer = temp
    return answer

set1 = set(['a','b','c'])
set2 = set(['d'])
set3 = set(['e','f'])
answer = cartesianProduct([set1, set2, set3])
print answer
