/*
* Calculator  e.g (1+3)*100- 20/(4+1)
**/
# This type of calculator question, has bracket and +-*/ and could be not separated by whitespace
def calculator(string):
    if not string:
        return 0
    lists = convert(string)
    temp = []
    while ')' in lists:
        index1 = lists.index(')')
        index2 = max(index for index, val in enumerate(lists[:index1]) if val == '(')
        result = calculate(lists[index2+1:index1])
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
            num = ord(lists[i][j]) - ord('0')
            while j+1 < len(lists[i]) and lists[i][j].isdigit():
                num = num*10 + ord(lists[i][j+1])-ord('0')
                j += 1
            j = 0
        elif len(lists[i])>1 and lists[i][0] == '-' and lists[i][1:].isdigit():
            j = 1
            num = ord(lists[i][j])-ord('0')
            while j+1 < len(lists[i]):
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

def convert(string):
    i = 0
    num = 0
    answer = []
    while i < len(string):
        if string[i] == '+' or string[i] == '-' or string[i] == '*' or string[i] == '/':
            answer.append(string[i])
        elif string[i] == '(' or string[i] == ')':
            answer.append(string[i])
        elif string[i].isdigit():
            num = ord(string[i])-ord('0')
            while i+1<= len(string) and string[i+1].isdigit():
                num = num*10+ord(string[i+1])-ord('0')
                i += 1
            answer.append(str(num))
            num = 0
        i += 1
    return answer

answer = calculator('(1 +3)* (-100) - (-20)/(4+ 1)')
print answer
