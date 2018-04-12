class Solution(object):
    def findRepeatedDnaSequences(self, s):
        answer = []
        cntdict = dict()
        map = {'A':0, 'C':1, 'G':2, 'T':3}
        num = 0
        for x in range(len(s)):
            num = (map[s[x]]+num*4)&0xFFFFF
            if x < 9:
                continue
            cntdict[num] = cntdict.get(num,0)+1
            if cntdict[num] == 2:
                answer.append(s[x-9:x+1])
        return answer