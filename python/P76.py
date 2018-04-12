class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ''
        if len(s) < len(t):
            return ''
        missing  =list(t)
        index = {}
        for each in t:
            index[each] = []
        start = 0
        end = len(s)-1
        for i in range(len(s)):
            if s[i] in t:
                if s[i] not in missing and index[s[i]] != []:
                    index[s[i]].pop(0)
                elif s[i] in missing:
                    missing.remove(s[i])
                index[s[i]].append(i)
            if missing == []:
                minnum = min(x[0] for x in index.values())
                maxnum = max(x[-1] for x in index.values())
                if maxnum-minnum < end-start:
                    end = maxnum
                    start = minnum
        if missing != []:
            return ''
        return s[start:end+1]
            
                