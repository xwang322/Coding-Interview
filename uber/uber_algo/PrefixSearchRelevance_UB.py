/*
* implement a prefix search - given a set of characters, return the top-10 most relevant results.
* Relevancy here being the shorter word is more relevant than a longer word. An empty prefix is not a valid input.
* 中途问了一下如果定义relevance为根据lexico order又应该怎么做的问题（即bathroom < baths，对于bath来说）。
* 思路很简单（当然如果我说的不对麻烦大噶指出来），shorter word relevance用BFS，lex-order用DFS会更简单一点。
* 然后讨论一下runtime，memory，为什么用trie之类的。
* 但是我的代码里面有bug，以及建议在codepair上面练习compile and run test。
* 我调试到面试结束前八到十分钟才bug free跑出想要的结果。所以就没有然后了，聊了如何全面测试我的解法和uber简介小哥就说我还有个会，就到这里吧，白白。
* 另外有一个细节，在word end的node用boolean indicator就好，千万不要存string，
* BFS的时候可以用一个queue存candidate node，一个queue来存对应prefix string来construct string。我面试结束之后才想起来这个也是蛮伤心的。
**/
# This is for relevant
def prefixsearch(lists, word, count):
    if not lists:
        return []
    trie = {}
    for string in lists:
        t = trie
        for char in string:
            if char not in t:
                t[char] = {}
            t = t[char]
        t['*'] = '*'
    t = trie
    for char in word:
        if char not in t:
            return []
        t = t[char]
    queue = []
    for key in t:
        queue.append((key, word, t[key]))
    answer = []
    curr = 0
    while queue:
        element, prev, currTrie = queue.pop(0)
        if element == '*':
            answer.append(prev)
            curr += 1
            if curr == count:
                return answer
        else:
            for each in currTrie.keys():
                queue.append((each, prev+element, currTrie[each]))
    return answer

answer = prefixsearch(['teaman','teahouse','tealeaf','teatree','teacup','redtea','teasale'],'tea',7)
print answer

# This is the lexi order
def prefixsearch(lists, word, count):
    if not lists:
        return []
    trie = {}
    for string in lists:
        t = trie
        for char in string:
            if char not in t:
                t[char] = {}
            t = t[char]
        t['*'] = '*'
    t = trie
    for char in word:
        if char not in t:
            return []
        t = t[char]
    stack = []
    for key in t:
        stack.append((key, word, t[key]))
    answer = []
    curr = 0
    while stack:
        element, prev, currTrie = stack.pop()
        if element == '*':
            answer.append(prev)
            curr += 1
            if curr == count:
                return answer
        else:
            for each in currTrie.keys():
                stack.append((each, prev+element, currTrie[each]))
    return answer

answer = prefixsearch(['teaman','teahouse','tealeaf','teatree','teacup','redtea','teasale'],'tea',7)
print answer
