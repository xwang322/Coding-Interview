class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if not s or len(s) <= 2:
            return len(s)
        dictionary = {}
        start = 0
        end = 1
        answer = 0
        dictionary[s[0]] = 1
        while start < end and end <= len(s)-1:
            dictionary[s[end]] = dictionary.get(s[end], 0)+1
            if len(dictionary.keys()) <= 2:
                answer = max(answer, sum(dictionary.values()))
            else:
                while start < end and len(dictionary.keys()) != 2:
                    dictionary[s[start]] -= 1
                    if dictionary[s[start]] == 0:
                        del dictionary[s[start]]
                    start += 1
            end += 1
        return answer
        