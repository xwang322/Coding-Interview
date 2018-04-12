class Solution(object):
    def maxProduct(self, words):
        nums = []
        for word in words:
            nums.append(sum(1<<(ord(x)-ord('a')) for x in set(word)))
        answer = 0
        for x in range(len(words)):
            for y in range(len(words)):
                if not (nums[x]&nums[y]):
                    answer = max(answer, len(words[x])*len(words[y]))
        return answer