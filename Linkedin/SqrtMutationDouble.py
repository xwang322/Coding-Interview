'''
实现sqrt(x) 没啥可说的
改动是输入x是整数，输出要求是float。float啊请注意，二分搜索的range怎么搞，输出精度怎么控制，稍微想一下啊同学们。然后怎么测。
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
        if [left, right, mid] == observation:
            return round(left, digit)
        else:
             observation = [left, right, mid]

answer = SquareRootDouble(58,3)
print answer
