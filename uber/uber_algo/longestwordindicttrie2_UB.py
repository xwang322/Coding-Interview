/*
* 另一题是给一个字典和一个字符串S，在字典的所有单词中找出一个最长的单词并且其所有字母都在S中出现过。面试官希望看到的是trie+dfs。
**/
import collections
def findLongestWordInDict(dictionary, string):
    if not string or not dictionary:
        return ''
    counter = collections.Counter(string)
    trie = {}
    for word in dictionary:
        t = trie
        for char in word:
            if char not in t:
                t[char] = {}
            t = t[char]
        t['#'] = '#'
    answer = []
    dfs(trie, string, answer, counter)


def dfs(trie, string, answer, counter):
    stack = []
    for char in trie:
        path = ''
        t = trie
        stack.append(char)
        while stack:
            element = stack.pop()
            if element not in counter:
                break
            if element == '#':
                answer.append(path)
            path += element
            t = t[element]
            stack.append(t)
