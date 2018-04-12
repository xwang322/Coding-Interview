class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        if (len1+len2)%2:
            return self.getkth(nums1, nums2, (len1+len2)/2+1)
        else:
            return (self.getkth(nums1, nums2, (len1+len2)/2) + self.getkth(nums1, nums2, (len1+len2)/2+1)) * 0.5
    
    def getkth(self, A, B, k):
        lenA = len(A)
        lenB = len(B)
        if lenA > lenB:
            return self.getkth(B, A, k)
        if lenA == 0:
            return B[k-1]
        if k == 1:
            return min(A[0], B[0])
        pa = min(k/2, lenA)
        pb = k - pa
        if A[pa-1] <= B[pb-1]:
            return self.getkth(A[pa:], B, pb)
        else:
            return self.getkth(A, B[pb:], pa)
  
        