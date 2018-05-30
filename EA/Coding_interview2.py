


#
# Your last C# code is saved below:
# using System;
#
# public class Test
# {
#   public static void Main()
#   {
#     Console.WriteLine("Hello");
#   }
# }
#
# In a file there are many words. Find 10 most frequent words in that file with at least a min length of 5 characters?
# and how many times it is being used and sorted.
'''
defgh 20
abcd  10
xxxxx 10
yyyy 8

print

abcd 10
defgh
'''

import collections
import heapq
def findTop10words(file):
    if not file:
        return []
    lines = file.split('\n')
    counter = {}
    for line in lines:
        words = line.split(' ')
        for word in words:
            if len(word) >= 5:
                if word in counter:
                    counter[word] += 1
                else:
                    counter[word] = 1
    '''
    heap = []
    for key in counter:
        print key, counter[key]
        if len(heap) < 3:
            heapq.heappush(heap, (counter[key], key))
        else:
            temp = heapq.heappop(heap)
            if temp[0] < counter[key]:
                heapq.heappush(heap, (counter[key], key))
            else:
                heapq.heappush(heap, temp)
    answer = []
    while heap:
        answer.append(heapq.heappop(heap)[1])
    '''
    temp = sorted(counter, key = lambda x:counter[x], reverse = True)
    for word in temp:
        print word, counter[word]
    part = temp[:3]
    print part
    new = sorted(part)
    print new
    for each in new:
        print each, counter[each]
    return answer

answer = findTop10words('this is a test large file, maximum size always larger than, Xiaodong Wang, parse parse larger larger, power, always large file is better')
print answer
