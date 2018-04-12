/*
* 是个人非常有礼貌的三哥。题目是电话号码,里扣要器的变种。
* 需要一个一个打印出所有10位号码的字母组合。如果用python的话，要用yield 来解。
**/
# first version is using return to get all combinations
def CombinationYield(length):
    dictionary = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    answer = []
    dfs(answer, dictionary, length, '')
    for each in answer:
        print each

def dfs(answer, dictionary, length, path):
    if len(path) == length:
        answer.append(path)
        return
    for i in dictionary.keys():
        for each in dictionary[i]:
            dfs(answer, dictionary, length, path+each)

CombinationYield(3)
# This will stackoverflow in CoderPad since length is 3
# So based on that, using yield to output all of them

dictionary = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
def CombinationYield(length):
    if length == 0:
        yield ''
    else:
        for path in CombinationYield(length-1):
            # 对于这道题目，其实不需要用dictionary映射数字到字母
            # 也就是说下面的两层for其实只是枚举了'a'-'z'的所有字母
            # 不过这里就按原来的写法好了
            for i in dictionary.keys():
                for each in dictionary[i]:
                    yield path+each

for answer in CombinationYield(10):
    print answer
/*
* 打印10位数的所有combination
* backtracking 秒
* 优化没弄出来... 小哥说用tail recursion
**/

def CombinationYield(length):
    dictionary = 'abcdefghijklmnopqrstuvwxyz'
    answer = []
    dfs(answer, dictionary, length, '')
    for each in answer:
        print each

def dfs(answer, dictionary, length, path):
    while length > 0:
        # 按原来的写法，但不处理最后一个字母
        for i in range(len(dictionary)-1):
            dfs(answer, dictionary, length-1, path+dictionary[i])
            # 最后一个字母使用尾递归
            # 重复利用当前栈的参数以避免创建新的调用栈
        path += dictionary[-1]
        length -= 1
    answer.append(path)

CombinationYield(10)
