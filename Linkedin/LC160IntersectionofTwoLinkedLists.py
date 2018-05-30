# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        length1 = 0
        length2 = 0
        if not headA or not headB:
            return None
        tempA = headA
        while tempA:
            length1 += 1
            tempA = tempA.next
        tempB = headB
        while tempB:
            length2 += 1
            tempB = tempB.next
        if length1 > length2:
            while length1 > length2:
                headA = headA.next
                length1 -= 1
        else:
            while length1 < length2:
                headB = headB.next
                length2 -= 1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        if not headA and not headB:
            return None
        return headA
