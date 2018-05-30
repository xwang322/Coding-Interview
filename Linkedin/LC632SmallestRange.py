'''
Given three sorted arrays A[], B[] and C[], find 3 elements i, j and k from A, B and C respectively such that max(abs(A[i] – B[j]),
abs(B[j] – C[k]), abs(C[k] – A)) is minimized. Here abs() indicates absolute value.
Example :
Input: A[] = {1, 4, 10} B[] = {2, 15, 20} C[] = {10, 12} Output: 10 15 10。 10 from A, 15 from B and 10 from C[br]Input: A[] = {20, 24, 100} B[] = {2, 19, 22, 79, 800} C[] = {10, 12, 23, 24, 119}
Output: 24 22 23。24 from A, 22 from B and 23 from C [br]
当时拿到这个有一点点小慌。因为是sorted array，就下意识想了个binary search(O(nlogn))的方法，感觉比BF(O(n^3))。可惜啊，说完想法，大哥不让这么做。说有O(n)的法子，再好好想想。于是就是我漫长的思考时间。大概用了5分钟，想到了3 pointers的方法。
但是具体怎么3 个pointer 还是不太明确。看着时间流逝真是心里滴血啊。。。不管怎样就硬上了。开始边实现边想。实现到一半，幸运的云开雾散了。原来就是每次移动3个pointer 里面最小的那个就好了。
记录整个过程找最近的3个数。3个数之中median没意义，距离主要由最小和最大决定。基本就是这个思路。很快编完就过了编程阶段。
'''
class Solution(object):
    def smallestRange(self, nums):
        if not nums:
            return []
        row = len(nums)
        heap = []
        tempmax = 0
        for i in range(row):
            heapq.heappush(heap, (nums[i][0], i, 0))
            tempmax = max(tempmax, nums[i][0])
        answer = [float('-inf'), float('inf')]
        while heap:
            temp = heapq.heappop(heap)
            if tempmax - temp[0] < answer[1] - answer[0]:
                answer[0] = temp[0]
                answer[1] = tempmax
            if temp[2] == len(nums[temp[1]])-1:
                return answer
            heapq.heappush(heap, (nums[temp[1]][temp[2]+1], temp[1], temp[2]+1))
            tempmax = max(tempmax, nums[temp[1]][temp[2]+1])
        return answer
