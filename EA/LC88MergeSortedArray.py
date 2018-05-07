class Solution(object):
    def merge(self, nums1, m, nums2, n):
        temp = m+n-1
        i = m-1
        j = n-1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[temp] = nums1[i]
                temp -= 1
                i -= 1
            else:
                nums1[temp] = nums2[j]
                j -= 1
                temp -= 1
        while j >= 0:
            nums1[temp] = nums2[j]
            temp -= 1
            j -= 1
        return
