class Solution(object):
    # bit manipulation
    '''
    def majorityElement(self, nums):
        answer = 0
        for i in range(32):
            count = 0
            for num in nums:
                temp = (num>>i)&1
                if temp == 1:
                    count += 1
                else:
                    count -= 1
            if i == 31 and count > 0:
                answer -= 1<<31
            elif count > 0 and i !=31:
                answer += (1<<i)
        return answer
    '''
    def majorityElement(self, nums):
        answer = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == answer:
                count += 1
            else:
                count -= 1
            if count == 0:
                answer = nums[i]
                count = 1
        return answer