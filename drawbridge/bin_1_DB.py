/*
Sort an array by number of 1s in the binary of integer, if number of 1s are same,
the smaller one should be placed first.
*Exampleinput [1,2,3,4,5]return [1,2,4,3,5]
**/

Code:
def reOrder(nums):
    nums = sorted(nums, key=lambda x: bin(x).count('1'))
    return nums
