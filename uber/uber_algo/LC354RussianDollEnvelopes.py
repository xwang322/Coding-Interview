class Solution(object):
    def maxEnvelopes(self, envelopes):
        ''' TLE
        if not envelopes:
            return 0
        envelopes = sorted(envelopes, key=lambda x:x[0])
        n = len(envelopes)
        dp = [1]*n
        for i in range(1, n):
            for j in range(i):
                if envelopes[i][0]>envelopes[j][0] and envelopes[i][1]>envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
        '''
        envelopes = sorted(envelopes, key=lambda (width, height):(width, -height))
        tails = []
        for width, height in envelopes:
            index = bisect.bisect_left(tails, height)
            if index == len(tails):
                tails.append(height)
            elif index == 0:
                tails[0] = height
            elif index != 0 and tails[index] > height:
                tails[index] = height
        return len(tails)
