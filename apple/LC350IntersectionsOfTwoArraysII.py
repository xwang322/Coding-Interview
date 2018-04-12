class Solution(object):
    def intersect(self, nums1, nums2):
        i,j = 0, 0
        answer = []
        nums1.sort()
        nums2.sort()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                answer.append(nums1[i])
                i += 1
                j += 1
        return answer
        
