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
        flag = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                flag = True
                break
        if flag:
            # find the distance from the head to intersection
            temp = head
            length = 0
            while temp != slow:
                temp = temp.next
                slow = slow.next
                length += 1
        else:
            temp = head
            length = 0
            while temp:
                temp = temp.next
                length += 1
        return length
