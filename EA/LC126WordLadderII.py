class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []
        wordSet = set(wordList)
        head = []
        head.append(beginWord)
        tail = []
        tail.append(endWord)
        wordSet.discard(beginWord)
        wordSet.discard(endWord)
        length = len(beginWord)
        alphabets = [chr(ord('a')+i) for i in range(26)]
        dictionary = collections.defaultdict(list)
        flag = False
        left_right = True
        while head:
            next_level = set()
            for i in range(len(head)):
                current = head.pop()
                for i in range(length):
                    for j in range(26):
                        temp = current[:i] + alphabets[j] + current[i+1:]
                        if temp in tail:
                            flag = True
                        if temp in tail or temp in wordSet:
                            if left_right:
                                dictionary[current].append(temp)
                            else:
                                dictionary[temp].append(current)
                        if temp in wordSet:
                            next_level.add(temp)
            if flag:
                break
            head = next_level
            for each in next_level:
                wordSet.discard(each)
            if len(head) > len(tail):
                head, tail = tail, head
                left_right = not left_right
        answer = []
        self.dfs(dictionary, answer, beginWord, endWord, [beginWord])
        return answer

    def dfs(self, dictionary, answer, beginWord, endWord, path):
        if beginWord == endWord:
			# check pylist.py for why use ':' but not simply append, one is reference, the other is content
            answer.append(path[:])
            return
        for word in dictionary[beginWord]:
            path.append(word)
            self.dfs(dictionary, answer, word, endWord, path)
            path.pop()
