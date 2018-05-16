# Round 1, input is a stream, (key,value) pair key is like k1, k2....value is timestamp, but just integers.
# Output the most 3 biggest values with their key, however, the key should be distinct. The timestamp might not come in ascending order.
# Example, the stream is like (k1, 1), (k2, 2), (k1, 5), (k3, 7), (k4, 3). In this case, results is (k3, k1, k4) even though k1 has 2 records, select the larger one, but cannot have 2 k1 in the final.
# My idea, priority queue immediately, interviewers mention I can use whatever language I like, so Python.
def FindTopK(stream, k):
    # For stream, I do not know the function, so I asked the interviewer, he mentioned, you can use hasNext and Next
    # the key is ip, the value is timestamp, but no need to define the class
    heap = []
    while stream.hasNext():
        newele = stream.next()
        if len(heap) < k:
            heapq.heappush(heap, (newele.timestamp, newele.ip))
        else:
            while heap:
                temp = []
                ele = heapq.heappop(heap)
                if newele.ip == ele[1]:
                    heapq.heappush(heap, (max(newele.timestamp, ele[0]), ele[1]))
                    break
                elif newele.timestamp < ele[0]:
                    temp.append(ele)
                    break
                else:
                    heapq.heappush(heap, (newele.timestamp, newele.ip))
                    temp.append(ele)
                while temp:
                    if len(heap) < k:
                        heapq.heappush(heap, temp.pop())
        return heap
# The interview asks, why pop not peek? I said they are the same, if you find out you need to pop, you still need to pop, but I have a "temp" to collect everything out and push back later.
'''
Follow up question, assume there are no global variables. This is on distributed machines, if we only allow 2 functions, map() and reduce()
map(function A => B), reduce(A, A)=>A. How to solve, only 4 minutes left, so could not come up with a solution. The interviewer gives a idea:
for example, there is a list, [1,1,2,4,4,5,6,7] how to tell the distinct items inside (convert to set), map(A) to nearby element, is same leaves one, if not leave both.
But here the input stream is not sorted, and also map and reduce can only operate on one record, cannot figure out. Done
