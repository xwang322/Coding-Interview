class Solution(object):
    def hammingDistance(self, x, y):
        binx = list(bin(x))[2:]
        biny = list(bin(y))[2:]
        answer = 0
        while len(binx) > 0 or len(biny) > 0:
            if len(binx) > 0:
                tempx = binx.pop()
            else:
                tempx = '0'
            if len(biny) > 0:
                tempy = biny.pop()
            else:
                tempy = '0'
            if tempx != tempy:
                answer += 1 
        return answer
        