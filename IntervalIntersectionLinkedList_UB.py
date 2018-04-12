'''
intervals_intersection in linked list format
'''
class ListNode(object):
     def __init__(self, start, end):
        self.start = start
        self.end = end
        self.next = None

class solution(object):
    def intervals_intersection(self, list1, list2):
        if not list1 or not list2:
            return []
        answer = []
        i = 0
        j = 0
        while list1 and list2:
            if list1.end <= list2.start or list2.end <= list1.start:
                if list1.end <= list2.start:
                    list1 = list1.next
                else:
                    list2 = list2.next
            else:
                answer.append((max(list1.start, list2.start), min(list1.end, list2.end)))
                if list1.end >= list2.end:
                    list1.start = list2.end
                    list2 = list2.next
                else:
                    list2.start = list1.end
                    list1 = list1.next
        final = []
        for each in answer:
            if final and final[-1][1]+1 == each[0]:
                temp = final.pop()
                final.append((temp[0], each[1]))
            final.append(each)
        return final

a = ListNode(1,2)
b = ListNode(5,8)
c = ListNode(10,12)
d = ListNode(15,19)
a.next = b
b.next = c
c.next = d
e = ListNode(2, 7)
f = ListNode(9,20)
e.next = f
x = solution()

answer = x.intervals_intersection(a, e)
print answer
