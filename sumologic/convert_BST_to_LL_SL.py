/*
* Given a binary search tree write an algorithm that converts the tree into a linked list which is space minimal.
**/
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preOrder(root):
stack = []
        answer = []
        while root or stack:
            if root:
                stack.append(root)
                answer.append(root.val)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return answer


    def inorderTraversal(self, root):
        answer = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                answer.append(node.val)
                root = node.right
        return answer


def ArraytoLinkedList(array):
    if not array:
        return None
    if len(array) == 1:
        return ListNode(array[0])
    head = ListNode(arrray[0])
    p = head
    doublelist = collections.deque(array)
    while p:
        node = doublelist.popleft()
        if node:
            p.next = ListNode(node.val)
            p = p.next
        else:
            p.next = None
    return head

def function(root):
    array = preOrder(root)
    head = ArraytoLinkedList(array)
    return head
