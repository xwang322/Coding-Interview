/*
* 第一题是给定一个array把所有的0移到后面去，一开始用了个不是最优的方法，问有没有办法优化，然后提出了一个最优解
**/
def MovingZeros(array):
    if not array:
        return []
    left, right = 0, len(array)-1
    while left <= right:
        if array[left] == 0:
            array[left], array[right] = array[right], array[left]
            right -= 1
        else:
            left += 1
    return array

answer = MovingZeros([0, 1, 0, 3, 5, 0, 9, 0])
print answer
