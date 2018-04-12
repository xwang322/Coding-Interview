class Solution(object):
    def lengthOfLongestSubstring(self, s):
        answer, start, end = 0, 0, 0
        count = {}
        for each in s:
            end += 1
            count[each] = count.get(each, 0)+1
            while count[each] > 1:
                count[s[start]] -= 1
                start += 1
            answer = max(answer, end-start)
        return answer
