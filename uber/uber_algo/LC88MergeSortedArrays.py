class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if not nums1:
            nums1 = nums2
            return
        if not nums2:
            return
        i = m-1
        j = n-1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[i+j+1] = nums1[i]
                i -= 1
            else:
                nums1[i+j+1] = nums2[j]
                j -= 1
        if i < 0:
            nums1[:j+1] = nums2[:j+1]
        return
        
