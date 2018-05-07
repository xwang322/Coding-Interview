'''
问了一遍fibonacci
'''
def Fib(n):
    if n == 0 or n == 1 or n == 2:
        return n
    temp1 = 1
    temp2 = 2
    for i in range(2, n):
        temp3 = temp2
        temp2 += temp1
        temp1 = temp3
    return temp2
