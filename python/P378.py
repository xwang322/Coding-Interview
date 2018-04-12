class Solution(object):
    def kthSmallest(self, matrix, k):
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            mid = (left+right)/2
            temp = sum(bisect.bisect_right(m, mid) for m in matrix)
            # two solutions
            if temp < k:
                left = mid+1
            else:
                right = mid
            '''
            if temp >= k:
                right = mid-1
            else:
                left = mid+1
            '''
        return left
