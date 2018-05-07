'''
算法部分给了一段文字，是graph类的题，楼主从来没见过加上紧张就崩了，题目大概就是要用indegree找root（indegree = 0）
'''
def FindRoot(edges):
    # from the first to the second, first is parent, second is child
    if not edges:
        return []
    answer = []
    nums = set()
    for edge in edges:
        nums.add(edge[0])
        nums.add(edge[1])
    temp = [0 for i in range(len(nums))]
    for edge in edges:
        temp[edge[1]] += 1
    for each in temp:
        if each == 0:
            answer.append(each)
    return answer
