/*
* Degree of an Array
* Given an array of n integers, we define its degree as the maximum frequency of
* any element in the array.
* For example, the array [1, 2, 3, 4, 2, 2, 3] has a degree of 3 because the number
* 2 occurs three times (which is more than any other number in the array).
* We want to know the size of the smallest subarray of our array such that the
* subarray's degree is equal to the array's degree.
* For example, the array [1, 2, 2, 3, 1] has a degree of 2 because 1 and 2 occur a
* maximal two times. There are two possible subarrays with this degree: [1, 2, 2, 3, 1]
* and [2, 2]. Our answer is the length of the smallest subarray, which is 2.
* Complete the function in the editor below. It has one parameter: an array of
* n integers, arr. The function must return an integer denoting the minimum size
* of the subarray such that the degree of the subarray is equal to the degree of the array.
* */
def findShortestSubArray(self, nums):
    counter = collections.Counter(nums)
    temp = []
    for key in counter.keys():
        if counter[key] == max(counter.values()):
            temp.append(key)
    degree = max(counter.values())
    if degree == 1:
        return 1
    answer = len(nums)
    for each in temp:
        count = 0
        first = len(nums)-1
        last = 0
        for index, num in enumerate(nums):
            if num == each and count == 0:
                first = index
                count += 1
            elif num == each and count == degree-1:
                last = index
            elif num == each:
                count += 1
        answer = min(answer, last-first+1)
    return answer
