'''
intersection of two arrays，我说用hashtable, time: O(n), space: O(n)
assume two arrays intersections contains duplicates
'''
def intersection(nums1, nums2):
    # sort and two pointer
    nums1.sort()
    nums2.sort()
    answer = []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            answer.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            i += 1
    return answer

import collections
def intersection(nums1, nums2):
    # use hashmap
    dict1 = collections.Counter(nums1)
    dict2 = collections.Counter(nums2)
    answer = []
    for num in dict1:
        if num in dict2:
            answer += [num] * min(dict1[num], dict2[num])
    return answer

answer = intersection([1, 2, 2, 1], [2, 2])
print answer
