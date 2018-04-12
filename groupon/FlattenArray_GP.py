/*
* 楼主面的是Full Stack, 题目是写一个Flatten Array.
* 输入是[1, 2, [3, 4], [4, [5]]]
* 输出是[1,2,3,4,4,5]
**/
def FlattenArray(lists):
    if not lists:
        return []
    answer = []
    for element in lists:
        if isinstance(element, int):
            answer.append(element)
        else:
            nextlist = FlattenArray(element)
            while nextlist:
                answer.append(nextlist.pop(0))
    return answer

answer = FlattenArray([1, 2, [3, 4], [4, [5]]])
print answer
