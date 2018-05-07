'''
给一个string，求里面的所有字符的所有permutation
'''
def StringPermutation(string):
    # assume thiere is non-duplicate char in a string
    if not string:
        return []
    if len(string) == 1:
        return [string]
    answer = []
    for index, letter in enumerate(string):
        answer += [letter + p for p in StringPermutation(string[:index] + string[index+1:])]
    return answer

answer = StringPermutation('abcds')
print answer

def StringPermutation(string):
    # assume thiere are duplicate chars in a string
    if not string:
        return []
    if len(string) == 1:
        return [string]
    answer = []
    for index, letter in enumerate(string):
        answer += [letter + p for p in StringPermutation(string[:index] + string[index+1:])]
    temp = set()
    final = []
    for each in answer:
        if each not in temp:
            final.append(each)
            temp.add(each)
    return final

answer = StringPermutation('abca')
print answer
