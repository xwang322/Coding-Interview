/*
* LC非常相似的题，设计计算器。给一个string，比如"8 + -3 * 5 / 2 - ( 2 * -2 ) + 3"
* 比如"8 + ( -3 * 5 / 2 - ( 2 * -2 ) + 3 )"
* 用whitespace分隔开，有正有负，有加减乘除，有小括号。
**/
# assume the input bracket is not connected with the number, everything is space separated
# take out every level of bracket by calculator function
def calculator(string):
    if not string:
        return 0
    lists = string.split()
    temp = []
    while ')' in lists:
        index1 = lists.index(')')
        index2 = max(index for index, val in enumerate(lists[:index1]) if val == '(')
        result = calculate(lists[index2+1: index1])
        lists[index2] = str(result)
        lists[index2+1:index1+1] = '#'
        for element in lists:
            if element != '#':
                temp.append(element)
        lists = temp
        temp = []
    return calculate(lists)

def calculate(lists):
    if not lists:
        return 0
    sign = '+'
    stack = []
    i = 0
    num = 0
    while i < len(lists):
        j = 0
        if lists[i].isdigit():
            num = ord(lists[i][j])-ord('0')
            while j+1 <= len(lists[i])-1 and lists[i][j+1].isdigit():
                num = num*10 + ord(lists[i][j+1])-ord('0')
                j += 1
            j = 0
        elif len(lists[i]) > 1 and lists[i][0] == '-' and lists[i][1:].isdigit():
            j = 1
            num = ord(lists[i][j])-ord('0')
            while j+1 <= len(lists[i])-1 and lists[i][j+1].isdigit():
                num = num*10 + ord(lists[i][j+1])-ord('0')
                j += 1
            num = -num
        if not lists[i].isdigit() or i == len(lists)-1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop()*num)
            elif sign == '/':
                if stack[-1]%num != 0:
                    if stack[-1]/num < 0:
                        stack.append(stack.pop()/num+1)
                    else:
                        stack.append(stack.pop()/num)
                else:
                    stack.append(stack.pop()/num)
            sign = lists[i]
            num = 0
        i += 1
    return sum(stack)

answer = calculator("8 + ( -3 * 5 / 2 - ( 2 * -2 ) + 3 )")
print answer
