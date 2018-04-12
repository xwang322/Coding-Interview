class Solution(object):
    def fourSumCount(self, A, B, C, D):
        count = collections.defaultdict(int)
        answer = 0
        for a in A:
            for b in B:
                count[a+b] += 1
        for c in C:
            for d in D:
                answer += count[-(c+d)]
        return answer