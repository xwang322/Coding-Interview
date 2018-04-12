class Solution(object):
    def countBits(self, num):
        answer = [0]
        for x in range(1, num+1):
            answer.append(answer[x>>1]+(x&1))
        return answer