class Solution(object):
    ''' for some reason the print is good, but return result is wired
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            wordList.append(endWord)
        queue = collections.deque([[beginWord, 1]])
        answer = 0
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                answer = length
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    if word[:i]+char+word[i+1:] in wordList and word[:i]+char+word[i+1:] != word:
                        wordList.remove(word[:i]+char+word[i+1:])
                        queue.append([word[:i]+char+word[i+1:], length+1])
        print answer
        return answer
    '''
    def ladderLength(self, beginWord, endWord, wordList):
        
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d
            
        def bfs_words(begin, end, dict_words):
            queue, visited = collections.deque([(begin, 1)]), set()
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
        print d
        return bfs_words(beginWord, endWord, d)