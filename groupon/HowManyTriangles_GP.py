/*
* 第二题是给定一个array，输出所有元素最多能组成几个不同的三角形？
**/
# assume the array is int array, brute force, no better solution
def HowManyTriangles(array):
    if not array:
        return 0
    array.sort()
    answer = []
    if len(array) <= 2:
        return 0
    for i in range(len(array)-2):
        for j in range(i+1, len(array)-1):
            for k in range(j+1, len(array)):
                if array[i] + array[j] > array[k]:
                    if (array[i], array[j], array[k]) not in answer:
                        answer.append((array[i], array[j], array[k]))
    return answer

answer = HowManyTriangles([1,2,2,3,4,5,6,7,8])
print answer
