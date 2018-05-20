class Solution(object):
    def findMaximumXOR(self, nums):
        trie = {}
        if not nums:
            return 0
        for num in nums:
            t = trie
            for i in range(32)[::-1]:
                current = (num>>i) & 1
                if current not in t:
                    t[current] = {}
                t = t[current]
        answer = 0
        for num in nums:
            t = trie
            tempsum = 0
            for i in range(32)[::-1]:
                curbit = (num>>i)&1
                if curbit^1 not in t: # the same as negation of curbit
                    t = t[curbit]
                else:
                    tempsum += (1<<i)
                    t = t[curbit^1]
            answer = max(answer, tempsum)
        return answer
