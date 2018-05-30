'''
给两个排好序的列表，找到前K个product最小的pair （lc上类似题应该是找最小的sum）
找到两个数组中前K个最小乘积。都是正数。不能有重复的。其实就是那个求和的变体。楼主打算用先推入K个到heap里的方法解决。
结果白人小哥不太理解说你这样不对。楼主刷这道题有点久了差点被带偏。花不少时间终于把小哥说服。然后写完就差不多到时间了。
感觉这轮本来可以多解决一道的。。
'''
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return []
        heap = []
        for num1 in nums1:
            for num2 in nums2:
                if len(heap) < k:
                    heapq.heappush(heap, (-num1*num2, [num1, num2]))
                else:
                    if heap and -heap[0][0] > num1*num2:
                        heapq.heappop(heap)
                        heapq.heappush(heap, (-num1*num2, [num1, num2]))
        answer = []
        while heap:
            answer.append(heapq.heappop(heap)[1])
        return answer
