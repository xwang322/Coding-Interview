class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        queue = [beginWord]
        answer = 1
        choices = [chr(ord('a')+i) for i in range(26)]
        length = len(beginWord)
        wordSet = set(wordList)
        while queue:
            size = len(queue)
            answer += 1
            for i in range(size):
                word = queue.pop(0)
                for j in range(length):
                    for k in choices:
                        newWord = word[:j] + k + word[j+1:]
                        if newWord in wordSet:
                            queue.append(newWord)
                            wordSet.discard(newWord)
                        if newWord == endWord:
                            return answer
        return 0
                
