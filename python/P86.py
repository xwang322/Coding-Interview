# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        head1 = ListNode(0)
        head2 = ListNode(0)
        temp = head
        p1 = head1
        p2 = head2
        while temp:
            if temp.val < x:
                p1.next = temp
                temp = temp.next
                p1 = p1.next
                p1.next = None
            else:
                p2.next = temp
                temp = temp.next
                p2 = p2.next
                p2.next = None
        p1.next = head2.next
        head = head1.next
        return head