class Solution(object):
    def groupAnagrams(self, strs):
        answer = []
        d = collections.defaultdict(list)
        for s in strs:
            d[tuple(sorted(s))].append(s)
        for each in d:
            answer.append([every for every in d[each]])
        return answer        
        