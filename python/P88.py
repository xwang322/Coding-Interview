class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if len(nums1) == 0 or len(nums2) == 0:
            nums1 += nums2
            return
        i, j = m-1, n-1
        end = m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[end] = nums2[j]
                j -= 1
            else:
                nums1[end] = nums1[i]
                i -= 1
            end -= 1
        if i < 0:
            nums1[:j+1] = nums2[:j+1]