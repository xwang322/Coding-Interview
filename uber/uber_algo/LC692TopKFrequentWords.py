class Solution(object):
    def topKFrequent(self, words, k):
        counts = collections.Counter(words)
        sorted_counts = sorted(counts, key=lambda word: (-counts[word], word))
        return sorted_counts[:k]