# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        self.head = head

    def getRandom(self):
        current = self.head
        node = current.next
        index = 1
        while node:
            if random.randint(0, index) == 0:
                current = node
            node = node.next
            index += 1
        return current.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
