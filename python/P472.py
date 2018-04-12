class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        answer = []
        self.Worddict = set(words)
        for word in words:
            self.Worddict.remove(word)
            if self.search(word):
                answer.append(word)
            self.Worddict.add(word)
        return answer
    
    
    def search(self, word):
        if word in self.Worddict:
            return True
        for index in range(1, len(word)):
            if word[:index] in self.Worddict and self.search(word[index:]):
                return True
        return False
        