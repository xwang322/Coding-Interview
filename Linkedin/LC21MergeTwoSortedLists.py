# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        temp1 = l1
        temp2 = l2
        dummy = ListNode(0)
        p = dummy
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                dummy.next = temp1
                temp1 = temp1.next
                dummy = dummy.next
            else:
                dummy.next = temp2
                temp2 = temp2.next
                dummy = dummy.next
        if temp1:
            dummy.next = temp1
        if temp2:
            dummy.next = temp2
        return p.next
