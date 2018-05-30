'''
linked list是否有环，follow up 有环的list怎么找长度
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def findCycleLength(self, head):
        if not head or not head.next:
            return 0
        slow = fast = head
        length1 = 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            length1 += 1
            if fast == slow:
                break
        if fast == slow:
            return length1
        return 0
