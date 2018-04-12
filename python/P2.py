# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        temp = 0
        carry = 0
        dummy = head = ListNode(0)
        while l1 is not None and l2 is not None:
            temp = (l1.val+l2.val+carry)%10
            carry = (l1.val+l2.val+carry)/10
            dummy.next = ListNode(temp)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            temp = (l1.val+carry)%10
            carry = (l1.val+carry)/10
            dummy.next = ListNode(temp)
            dummy = dummy.next
            l1 = l1.next
        while l2 is not None:
            temp = (l2.val+carry)%10
            carry = (l2.val+carry)/10
            dummy.next = ListNode(temp)
            dummy = dummy.next
            l2 = l2.next
        if carry:
            dummy.next = ListNode(carry)
        return head.next