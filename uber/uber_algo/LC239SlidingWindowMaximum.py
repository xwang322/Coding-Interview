class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums or not k:
            return nums
        answer = []
        queue = []
        for i, v in enumerate(nums):
            while queue and queue[0]<=i-k:
                queue.pop(0)
            while queue and nums[queue[-1]]<= v:
                queue.pop()
            queue.append(i)
            if i+1 >= k:
                answer.append(nums[queue[0]])
        return answer
