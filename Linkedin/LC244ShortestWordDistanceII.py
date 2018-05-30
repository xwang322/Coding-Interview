class WordDistance(object):

    def __init__(self, words):
        self.dictionary = collections.defaultdict(list)
        for index, word in enumerate(words):
            if word not in self.dictionary:
                self.dictionary[word] = []
            self.dictionary[word].append(index)

    def shortest(self, word1, word2):
        list1 = self.dictionary[word1]
        list2 = self.dictionary[word2]
        i = j = 0
        answer = float('inf')
        while i < len(list1) and j < len(list2):
            answer = min(answer, abs(list1[i]-list2[j]))
            if list1[i] < list2[j]:
                i += 1
            else:
                j += 1
        return answer



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
