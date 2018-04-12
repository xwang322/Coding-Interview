class Solution(object):
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        answer = []
        for num in set(nums1):
            if num in set(nums2):
                answer.append(num)
        return answer
                
        