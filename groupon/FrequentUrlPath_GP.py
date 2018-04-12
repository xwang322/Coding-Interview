/*
* 第一轮是返回一个frequent url path pattern的问题，用map就好了，很简单，但是我写的不知道哪里有bug。。
**/
import random
import string
def FrequentURLPath(path):
    if not path:
        return ''
    dictionary = {}
    backchoice = string.ascii_letters + string.digits
    dictionary[path] = 'http://FrequentPath.com/'+''.join(random.choice(backchoice) for i in range(6))
    return dictionary[path]

answer = FrequentURLPath('http://leetcode/problem/shit')
print answer
