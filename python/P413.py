class Solution(object):
    def numberOfArithmeticSlices(self, A):
        size = len(A)
        if size < 3:
            return 0
        answer = count = 0
        delta = A[1] - A[0]
        for x in range(2, size):
            if A[x]-A[x-1] == delta:
                count += 1
                answer += count
            else:
                delta = A[x] - A[x-1]
                count = 0
        return answer