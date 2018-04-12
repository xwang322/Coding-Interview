# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Queue import PriorityQueue
class Solution(object):
    # Python Heap
    ''' 
    def mergeKLists(self, lists):
        if not lists:
            return None
        heap = []
        dummy = ListNode(0)
        p = dummy
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))
        while heap:
            p.next = heapq.heappop(heap)[1]
            p = p.next
            if p.next:
                heapq.heappush(heap, (p.next.val, p.next))
        return dummy.next
    #Python PQ solution
    def mergeKLists(self, lists):
        if not lists:
            return None
        dummy = ListNode(0)
        p = dummy
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))
        while not q.empty():
            p.next = q.get()[1]
            p = p.next
            if p.next:
                q.put((p.next.val, p.next))
        return dummy.next
    '''
    # Python DC
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists)/2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(left, right)
        
        
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        p = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                p.next = list1
                list1 = list1.next
                p = p.next
            else:
                p.next = list2
                p = p.next
                list2 = list2.next
        if not list1:
            p.next = list2
        else:
            p.next = list1
        return dummy.next
