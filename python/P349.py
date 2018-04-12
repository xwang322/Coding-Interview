class Solution(object):
    ''' TP
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        i,j = 0,0
        answer = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                answer.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return list(set(answer))
    '''
    def intersection(self, nums1, nums2):
        nums2.sort()
        answer = []
        for num in nums1:
            if self.bs(nums2, num) and num not in answer:
                answer.append(num)
        return answer
    
    def bs(self, nums2, num):
        left = 0
        right = len(nums2)-1
        while left <= right:
            mid = (left+right)/2
            if nums2[mid] == num:
                return True
            elif nums2[mid] < num:
                left = mid+1
            else:
                right = mid-1
        return False