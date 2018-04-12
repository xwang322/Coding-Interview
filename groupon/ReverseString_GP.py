/*
* 第一题"I like groupon" -> "I ekil nopuorg"应该是CC150原题, follow up: how to test, give edge cases
**/
def ReverseString(string):
    if not string:
        return ''
    answer = []
    for item in string.split():
        answer.append(item[::-1])
    return ' '.join(answer)

answer = ReverseString('I like groupon')
print answer
