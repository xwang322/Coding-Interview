# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        return self.mergehelper(lists, 0, len(lists)-1)
        
    def mergetwolists(self, l1, l2):
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next
    
    def mergehelper(self, lists, begin, end):
        if begin > end:
            return None
        if begin == end:
            return lists[begin]
        return self.mergetwolists(self.mergehelper(lists, begin, (begin+end)/2), self.mergehelper(lists, (begin+end)/2+1, end))