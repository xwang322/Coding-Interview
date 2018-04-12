/*
* 第一题是将一个有序数组乘方后返回import bisect
**/
def SortedSquareArray(array):
    left = right = bisect.bisect_left(array, 0)
    print left, right
    answer = []
    while right-left < len(array):
        if right == len(array):
            while left > 0:
                answer.append(array[left-1]**2)
                left -= 1
            return answer
        if abs(array[left-1]) < abs(array[right]):
            answer.append(array[left-1]**2)
            left -= 1
        else:
            answer.append(array[right]**2)
            right += 1
    return answer

answer = SortedSquareArray([-9, -7, -1, 0, 1, 3, 9])
print answer
