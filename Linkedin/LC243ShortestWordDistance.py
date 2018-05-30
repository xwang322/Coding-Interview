class Solution(object):
    def shortestDistance(self, words, word1, word2):
        dictionary = collections.defaultdict(list)
        for index, word in enumerate(words):
            dictionary[word].append(index)
        list1 = dictionary[word1]
        list2 = dictionary[word2]
        i = j = 0
        answer = float('inf')
        while i < len(list1) and j < len(list2):
            answer = min(answer, abs(list1[i]-list2[j]))
            if list1[i] <= list2[j]:
                i += 1
            else:
                j += 1
        return answer
