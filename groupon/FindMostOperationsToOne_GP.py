/*
* 是本版的高频题，就是对于任何一个数，如果是偶数的话就除以2，是奇数的话乘以3+1，最后这么算经过若干次运算总会变成1，
* 然后给你一个数字范围，从m到n，要你计算这个范围内所有数字这么算成1之后，需要运算次数最多的那个数的次数 就比较简单，
* 从第一个数开始死算，用hashmap把这个数的结果和所有中间数的结果全部存起来即可，之后如果碰到存起来的数就不用算了，直接return
**/

def FindMostOperations(m, n):
    dictionary = {}
    for i in range(m, n+1):
        record(dictionary, i, 0)
    answer = []
    for key in dictionary:
        if dictionary[key] == max(dictionary.values()):
            answer.append(key)
    return answer

def record(dictionary, number, ops):
    if number == 1:
        return 0
    if number in dictionary:
        return dictionary[number]
    temp = 0
    if number != 1:
        if number%2:
            temp = number*3+1
            dictionary[number] = record(dictionary, temp, ops)+1
        else:
            temp = number/2
            dictionary[number] = record(dictionary, temp, ops)+1
    return dictionary[number]

answer = FindMostOperations(2,6)
print answer
 
