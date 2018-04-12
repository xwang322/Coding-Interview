class Solution(object):
    def minWindow(self, s, t):
        if not t or not s:
            return s
        if len(t) > len(s):
            return ''
        counter_t = collections.Counter(t)
        counter_s = collections.Counter(s)
        if not all(key in counter_s.keys() for key in counter_t.keys()):
            return ''
        answer = float('Inf')
        left = 0
        right = 0
        answer_string = ''
        while right <= len(s):
            if all(map(lambda x: True if x<=0 else False, counter_t.values())):
                if answer > right-left:
                    answer = right-left
                    answer_string = s[left:right]
                char = s[left]
                if char in counter_t:
                    counter_t[char] += 1
                left += 1
            else:
                if right == len(s):
                    break
                char = s[right]
                if char in counter_t:
                    counter_t[char] -= 1
                right += 1
        return answer_string
