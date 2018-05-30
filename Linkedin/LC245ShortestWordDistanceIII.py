class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        dictionary = collections.defaultdict(list)
        for index, word in enumerate(words):
            dictionary[word].append(index)
        if word1 != word2:
            list1 = dictionary[word1]
            list2 = dictionary[word2]
            i = j = 0
            answer = float('inf')
            while i < len(list1) and j < len(list2):
                answer = min(answer, abs(list1[i]-list2[j]))
                if list1[i] >= list2[j]:
                    j += 1
                else:
                    i += 1
        else:
            list1 = dictionary[word1]
            answer = float('inf')
            for i in range(len(list1)-1):
                answer = min(answer, list1[i+1]-list1[i])
        return answer
        
