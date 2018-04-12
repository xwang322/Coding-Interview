# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = p = ListNode(None)
        while l1 and l2:
            temp, carry = (l1.val+l2.val+carry)%10, (l1.val+l2.val+carry)/10
            temp_node = ListNode(temp)
            p.next = temp_node
            p = p.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            temp, carry = (l1.val+carry)%10, (l1.val+carry)/10
            temp_node = ListNode(temp)
            p.next = temp_node
            p = p.next
            l1 = l1.next
        while l2:
            temp, carry = (l2.val+carry)%10, (l2.val+carry)/10
            temp_node = ListNode(temp)
            p.next = temp_node
            p = p.next
            l2 = l2.next
        if carry:
            temp_node = ListNode(carry)
            p.next = temp_node
        return dummy.next
