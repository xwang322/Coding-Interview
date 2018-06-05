class Solution(object):
    def minWindow(self, s, t):
        if len(s) < len(t):
            return ''
        counter_t = collections.Counter(t)
        start = 0
        end = 0
        counter_s = {}
        answer = len(s)+1
        answer_string = ''
        flag = False
        while start <= end:
            while not all(key in counter_s and counter_s[key] >= counter_t[key] for key in counter_t):
                if end == len(s)-1:
                    counter_s[s[end]] = counter_s.get(s[end], 0)+1
                    end += 1
                    flag = True
                    break
                counter_s[s[end]] = counter_s.get(s[end], 0)+1
                end += 1
            while all(key in counter_s and counter_s[key] >= counter_t[key] for key in counter_t):
                counter_s[s[start]] -= 1
                start += 1
            if end-start+1 < answer:
                answer = end-start+1
                answer_string = s[start-1:end]
            if flag:
                break
        return answer_string
