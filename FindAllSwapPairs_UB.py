'''
第二轮出了些事故，犹太小哥说我电话打不通（excuse me ？） 后来拖了16分钟才面试上。
题目是给一个数组比如[9,5,8,4], 输出是找出所有的pair，使得index i < index j, 但 value i > value j.
比如这个例子有[9,5][9,8],[9,4],,,[5,4],[8,4]. 想了半天是在没有想到更好的方法，最后用PriorityQueue + 记忆化搜索解之。
到现在都没想到更好的方法，如果地里的大佬有更好的方法，希望能分享一下） 写完后本来应该有时间问问题的，
但由于之前拖了时间，小哥说他马上又有另外一场面试，就草草收场了。
'''
import heapq
def FindAllPairs(nums):
    if not nums:
        return []
    heap = []
    for index, num in enumerate(nums):
        heapq.heappush(heap, (num, index))
    answer = []
    order = 0
    while heap:
        element, curr = heapq.heappop(heap)
        if curr != order:
            temp = []
            while heap:
                temp1, temp2 = heapq.heappop(heap)
                if temp2 < curr and temp1 > element:
                    answer.append((temp1, element))
                    temp.append((temp1, temp2+1))
                else:
                    temp.append((temp1, temp2))
            for pair in temp:
                heapq.heappush(heap, pair)
        order += 1
    return answer

answer = FindAllPairs([4,2,8,9,0])
print answer
