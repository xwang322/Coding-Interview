class Solution(object):
    def swapPairs(self, head):
        if not head:
            return None
        prev = dummy = ListNode(0)
        prev.next = head
        while head and head.next:
            curr = head.next
            head.next = curr.next
            curr.next = head
            prev.next = curr
            head = head.next
            prev = curr.next
        return dummy.next