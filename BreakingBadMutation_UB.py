'''
刚刚结束的电面，感觉有点崩的。breakingbad，好像之前面经出现很多次，但是没有详细的介绍，把题想简单了。。
具体介绍一下这个题， input是String[] array(大小写都有), 和一个String name（全小写）[br]输出要求有点复杂，在name一个个substring里找，
如果这个substring没有在array里出现过，就直接输出。如果在array里出现过，就找尽量长的可以在array里匹配得到的，
然后把第一个字母变成大写并且前后加上[]符号再输出。[br]比如array = {"b", "Bc", "e"} name = "abcde"; output就是a[Bc]d[E]
这里因为b可以匹配到b，bc可以匹配到bc而且更长所以答案就是这样。
开始太紧张了做了一会才开始急急忙忙的写Trie。
其实这题很难。主要难在你在name里遇到的prefix可能不是最优的。比方说：array = {"b", "Bc", "cde"}  name = "abcde";
如果你用greedy找到了"Bc", 你就miss了c开始的prefix了。
'''
def BreakingBad(name, array):
    trie = {}
    for string in array:
        t = trie
        for char in string:
            if char.lower() not in t:
                t[char.lower()] = {}
            t = t[char.lower()]
        t['#'] = len(string)
    answer = []
    length = 0
    i = 0
    while i < len(name):
        if name[i] not in trie:
            answer.append(name[i])
            i += 1
        else:
            temp = 0
            temp_string = ''
            t = trie
            while i<len(name) and name[i] in t:
                temp_string += name[i]
                t = t[name[i]]
                if '#' in t:
                    temp = t['#']
                i += 1
            if temp:
                answer.append('['+temp_string[0].upper()+temp_string[1:].lower()+']')
            else:
                answer.append(name[i-len(temp_string):i])
    return ''.join(answer)

#answer = BreakingBad('abcde', ['b','Bc','e'])
#answer = BreakingBad('abcde', ['b','Bc','cde'])
answer = BreakingBad('abcdeddertte', ['b','bc','cde','e','tt','ertt','ddr'])
print answer
