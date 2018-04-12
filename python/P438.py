class Solution(object):
    def findAnagrams(self, s, p):
        answer = []
        pcounter = collections.Counter(p)
        scounter = collections.Counter(s[0:len(p)-1])
        for i in range(len(p)-1,len(s)):
            scounter[s[i]] += 1
            if scounter == pcounter:
                answer.append(i-len(p)+1)
            scounter[s[i-len(p)+1]] -= 1
            if scounter[s[i-len(p)+1]] == 0:
                del scounter[s[i-len(p)+1]]
        return answer