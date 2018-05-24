'''
给一个input array, 一个数, 找到subarray,这个subarray的和的模数最大。
例如: input array: 3,3,5,6,7,9. mod: 5. 返回: 3,5,6, 因为(3 + 5 + 6) % 5 = 4. 可以有多种解，返回一种就行。
'''
def subMaxModule(nums, module):
    if not module or not nums:
        return []
    nums1 = list(map((lambda x : x%module), nums))
    for i in range(module-1, 0, -1):
        target = i
        dictionary = {0 : -1}
        total = 0
        for j, num in enumerate(nums1):
            total += num
            m = total%target
            if m not in dictionary:
                dictionary[m] = j
            elif dictionary[m]+1 < j:
                return nums[dictionary[m]+1: j+1]
    return []
	
answer = subMaxModule([3,3,5,6,7,9], 5)
print answer
