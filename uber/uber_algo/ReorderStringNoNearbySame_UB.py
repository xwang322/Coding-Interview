/* Google interview question, also for Uber
* 国人大哥的电面，感觉是放水了。
* 先问了10分钟behavior，如何解决conflict，工作中的challenge。
* coding：给一个string，reorder里面的字母，相邻的字母不相同。例如aabb -> abab || baba, aaabbc -> ababac etc.
* 输入的string保证能有一个valid的输出。多种结果只要返回一个即可。
* solution：O(N) pass一遍整个string，一个map<char, int>记每个的char出现的次数。然后就类似k merged list，每次取剩下的char里面出现次数最多的。可以用priority queue做下优化这样每次找到剩下最多char时间就是lgK，K是unique char。需要一个char prevChar来判断取的char和前一个char是否相同。
* e.g
* aaabbc -> a:3, b:2, c:1 -> 取a -> a -> a:2, b:2, c:1 -> 取b -> ab -> a:2, b:1, c:1 ->取a -> aba -> a:1, b:1, c:1 -> 取b -> abab -> a:1, c:1 -> 取a -> ababa -> c:1 -> 取c -> ababac。
* 一小时不到接到hr通知onsite
* aaac return ‘’?
* aaab
* aabc
* paaaabcnsallsaa
* abac
* abca
**/
import heapq
import collections
def reorder_string(string):
    dictionary = collections.Counter(string)
    heap = []
    for key in dictionary:
        heapq.heappush(heap, (-dictionary[key], key))
    temp = ''
    answer = []
    while heap:
        number, element = heapq.heappop(heap)
        if element != temp:
            answer.append(element)
            temp = element
            if number+1 < 0:
                heapq.heappush(heap, (number+1, element))
        else:
            if heap:
                another_number, another_element = heapq.heappop(heap)
                answer.append(another_element)
                temp = another_element
                if another_number+1 < 0:
                    heapq.heappush(heap, (another_number+1, another_element))
                heapq.heappush(heap, (number, element))
            else:
                return ''
    return ''.join(answer)

answer = reorder_string('paaaabcnsallsaa')
print answer
