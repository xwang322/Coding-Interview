'''
given a tree structrue {'s1':'([])','s2:{s3:'{[(]}'}','s4':''}, 判断这个given tree是否是valid tree（即里面的元素都是valid parentheses）.
'''
def validTreeStrucutre(string):
    if not string:
        return True
    candidates = []
    for each in string:
        result = nestedIterator(each)
        candidates.append(result)
    for each in candidates:
        if isValid(each) == False:
            return False
    return True

def nestedIterator(string):
    clean = ''
    for char in string:
        if char != ' ':
            clean += char
    str_list = clean.split(':')
    if len(str_list) < 2:
        return None
    elif len(str_list) == 2:
        return str_list[1]
    else:
        temp = str_list[1][0]
        if temp == '(' and str_list[-1][-1] != ')':
            return None
        if temp == '{' and str_list[-1][-1] != '}':
            return None
        if temp == '[' and str_list[-1][-1] != ']':
            return None
        index1 = len(str_list[0])+1
        return nestedIterator(clean[index1:-1])

def isValid(s):
    if not s:
        return True
    stack = []
    for char in s:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        elif char == ')' or char == '}' or char == ']':
            if not stack:
                return False
            elif char == ')':
                if stack[-1] != '(':
                    return False
                stack.pop()
            elif char == ']':
                if stack[-1] != '[':
                    return False
                stack.pop()
            elif char == '}':
                if stack[-1] != '{':
                    return False
                stack.pop()
    if not stack:
        return True
    return False

answer = validTreeStrucutre(['s1:([])','s2:{s3:{[(]}}','s4:'])
print answer
