class Solution(object):
    def leastInterval(self, tasks, n):
        n += 1
        counts = collections.Counter(tasks)
        answer = 0
        heap = []
        for key in counts:
            heapq.heappush(heap, -counts[key])
        while heap:
            stack = []
            count = 0
            for i in range(n):
                if heap:
                    element = heapq.heappop(heap)
                    count += 1
                    if element < -1:
                        stack.append(element+1)
            while stack:
                heapq.heappush(heap, stack.pop())
            if heap:
                answer += n
            else:
                answer += count
        return answer
        
