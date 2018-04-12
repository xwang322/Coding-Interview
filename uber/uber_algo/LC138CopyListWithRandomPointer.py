# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        temp = head
        dictionary = {}
        dictionary[id(None)] = None
        while temp:
            dictionary[id(temp)] = RandomListNode(temp.label)
            temp = temp.next
        temp = head
        while temp:
            node = dictionary[id(temp)]
            node.next = dictionary[id(temp.next)]
            node.random = dictionary[id(temp.random)]
            temp = temp.next
        return dictionary[id(head)]