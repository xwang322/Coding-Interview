'''
* This function determines if the braces ('(' and ')') in a string are properly matched.
* it ignores non-brace characters.
* Some examples:
* "()()()()" -> true
* "((45+)*a3)" -> true
* "(((())())" -> false
'''

def parentheseMatch(string):
    if not string:
        return True
    count = 0
    for i in range(len(string)):
        if string[i] == '(':
            count += 1
        elif string[i] == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0

answer = parentheseMatch('(((())())')
print answer
