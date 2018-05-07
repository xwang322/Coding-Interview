# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # O(n) space
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        visited = set()
        while headA:
            visited.add(headA.val)
            headA = headA.next
        while headB:
            if headB.val in visited:
                return headB
            headB = headB.next
        return None


class Solution(object):
    # O(1) space
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        length1 = 0
        length2 = 0
        tempA = headA
        tempB = headB
        while tempA:
            length1 += 1
            tempA = tempA.next
        while tempB:
            length2 += 1
            tempB = tempB.next
        if length1 >= length2:
            for i in range(length1 - length2):
                headA = headA.next
        else:
            for i in range(length2 - length1):
                headB = headB.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
