'''
面经题，求两个interval lists的intersection
类似于https://careercup.com/question?id=5682567566065664
输入自己决定，要在codepad把结果run出来。
'''

import collections
def intervals_intersection(list1, list2):
    if not list1 or not list2:
        return []
    list1 = collections.deque(list1)
    list2 = collections.deque(list2)
    answer = []
    i = 0
    j = 0
    while i <= len(list1)-1 and j <= len(list2)-1:
        if list1[i][1] <= list2[j][0] or list2[j][1] <= list1[i][0]:
            if list1[i][1] <= list2[j][0]:
                list1.popleft()
            else:
                list2.popleft()
        else:
            answer.append((max(list1[i][0], list2[j][0]), min(list1[i][1], list2[j][1])))
            if list1[i][1] >= list2[j][1]:
                temp1 = list1.popleft()
                temp2 = list2.popleft()
                list1.appendleft((temp2[1], temp1[1]))
            else:
                temp1 = list1.popleft()
                temp2 = list2.popleft()
                list2.appendleft((temp1[1], temp2[1]))
    final = []
    for each in answer:
        if final and final[-1][1]+1 == each[0]:
            temp = final.pop()
            final.append((temp[0], each[1]))
        final.append(each)
    return final

answer = intervals_intersection([(1,2), (5,8), (10,12), (15,19)], [(2, 7), (9,20)])
print answer
