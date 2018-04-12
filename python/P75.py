class Solution(object):
    def sortColors(self, nums):
        if not nums or len(nums) == 1:
            return 
        red = 0
        blue = len(nums)-1
        i = 0
        while i <= len(nums)-1:
            if nums[i] == 0 and i > red:
                nums[red], nums[i] = nums[i], nums[red]
                red += 1
                i -= 1
            elif nums[i] == 2 and i < blue:
                nums[blue], nums[i] = nums[i], nums[blue]
                blue -= 1
                i -= 1
            i += 1
            
                