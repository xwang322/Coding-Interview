# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    '''
    def isPalindrome(self, head):
        lists = []
        while head:
            lists.append(head.val)
            head = head.next
        return lists == lists[::-1]
    '''
    def isPalindrome(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
