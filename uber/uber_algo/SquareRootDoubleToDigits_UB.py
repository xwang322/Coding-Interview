'''
回报地里，45分钟的电面，听声音和名字应该是一个美国小姐姐，上来先介绍了一下自己在做什么，
然后上题目： 实现 开方(数字, 精确度) , 比如 开方（6，3）-> 2.449 。
写了一个简单暴力的，然后问怎么优化。利口里面虽然也有 开方 的题目，但是只要求整数
第二轮 coding，特别好看的白人小姐姐！算square root，先是return int，然后变成return k decimal place
'''
def SquareRootDouble(number, digit):
    if not number:
        return 0
    left = round(0, digit+1)
    right = round(number,digit+1)
    i = 0
    observation = [left, 0, right]
    while True:
        mid = round((left+right)/2, digit+1)
        if mid**2 == number:
            return mid
        elif mid**2 > number:
            right = mid
        else:
            left = mid
        print [left, right, mid], observation
        if [left, right, mid] == observation:
            return round(left, digit)
        else:
             observation = [left, right, mid]

answer = SquareRootDouble(58,3)
print answer
