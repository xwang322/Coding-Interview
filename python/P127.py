from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d
            
        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i+1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0
        
        d = construct_dict(wordList)
        return bfs_words(beginWord, endWord, d)
    '''
    def ladderLength(self, beginWord, endWord, wordList): 
        if endWord not in wordList:
            return 0
        wordList = set(wordList)
        length = len(beginWord)
        this_level = [beginWord]
        next_level = []
        visited = set()
        answer = 1
        while this_level:
            while this_level:
                element = this_level.pop(0)
                if element == endWord:
                    return answer
                for each in wordList:
                    if each not in visited:
                        for i in range(length):
                            if element[:i]+element[i+1:] == each[:i]+each[i+1:]:
                                next_level.append(each)
                                visited.add(each)
            this_level = next_level
            next_level = []
            answer += 1
        return 0
    '''