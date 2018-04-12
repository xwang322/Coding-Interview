/*
* prefix calculator
**/
def prefixCalculator(string):
    tokens = string.split(' ')
    stack = []
    total = None
    for token in tokens:
        if token.isdigit():
            temp = int(token)
            if not total:
                total = temp
            else:
                total = evaluate(stack.pop(), total, temp)
        else:
            stack.append(token)
    return total

def evaluate(operator, first, second):
    if operator == '+':
        return first+second
    elif operator == '-':
        return first-second
    elif operator == '*':
        return first*second
    elif operator == '/':
        return first/second

answer = prefixCalculator('+ / 6 2 4 - 6')
print answer
# Or using regex
def calc_eval(exp):
    m = regex.match(r'\(([-+\/\*]) ((?R)) ((?R))\)|(\d+)|[-+\/\*]', exp)
    if all(map(m.group, [1, 2, 3])):  # exp is a procedure call
        return eval(' '.join([str(calc_eval(m.group(i))) for i in [2, 1, 3]]))
    return eval(exp) if m.group(4) else exp  # exp is a number / an operator
