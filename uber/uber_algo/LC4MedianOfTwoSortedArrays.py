class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        if (m+n)%2:
            return self.FindElement(nums1, nums2, (m+n)/2)
        else:
            return (self.FindElement(nums1, nums2, (m+n)/2)+self.FindElement(nums1, nums2, (m+n)/2-1))/2.0

    def FindElement(self, nums1, nums2, kth):
        if len(nums1) > len(nums2):
            return self.FindElement(nums2, nums1, kth)
        if len(nums1) == 0:
            return nums2[kth]
        if kth == 0:
            return min(nums1[0], nums2[0])
        len1 = len(nums1)
        len2 = len(nums2)
        pa = min(len1, (kth+1)/2)
        pb = kth+1-pa
        if nums1[pa-1] <= nums2[pb-1]:
            return self.FindElement(nums1[pa:], nums2, kth-pa)
        else:
            return self.FindElement(nums1, nums2[pb:], kth-pb)
