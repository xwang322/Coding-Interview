class Solution(object):
    def merge(self, nums1, m, nums2, n):
        temp = [0 for i in range(m+n)]
        i = 0; j = 0; k = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                temp[k] = nums1[i]
                i += 1
            else:
                temp[k] = nums2[j]
                j += 1
            k += 1
        if i == m:
            while k < m+n:
                temp[k] = nums2[j]
                j += 1
                k += 1
        else:
            while k < m+n:
                temp[k] = nums1[i]
                i += 1
                k += 1
        for i in range(m+n):
            nums1[i] = temp[i]