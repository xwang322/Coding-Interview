'''
利扣239
'''
def maxSlidingWindow(self, nums, k):
    queue = []
    answer = []
    for index, num in enumerate(nums):
        while queue and queue[0] <= index-k:
            queue.pop(0)
        while queue and nums[queue[-1]] < num:
            queue.pop()
        queue.append(index)
        if index+1 >= k:
            answer.append(nums[queue[0]])
    return answer
