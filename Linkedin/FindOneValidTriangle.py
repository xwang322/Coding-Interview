'''
寻找数组里有没有三个数字可以组成一个三角形。楼主当时看到就以为是原题要找出所有可以组成三角形的三个数组，哗啦啦讲了一大堆，
小哥说你这个复杂度太高了，纠结了一下还能怎么简化，结果发现人家只是让找有没有一组数字满足要求即可。。- -
时间不太够了就赶紧写了写完事。惨痛的教训：不要看到原题就激动的去做，一定要好好听完题。。
'''
def findOneTriangle(nums):
    if not nums:
        return 0
    nums.sort()
    for i in range(len(nums)-1, 1, -1):
        left = 0
        right = i-1
        while left < right:
            if nums[left] + nums[right] > nums[i]:
                return True
            else:
                left += 1
    return False
