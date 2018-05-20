               8
              / \
             2   3
            / \   \
           1   2   2
                \   \
                 1   2
                / \
               2   2
              /   /
             1   1
result: 2, 1
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

hash() :
     hash(val) * left.hash() * right.hash();

def FindDuplicate(root):
    if not root:
        return []
    record = set()
    stack = []
    dictionary = collections.defaultdict(list)
    while root or stack:
        if root:
            if root.val not in record:
                stack.append(root)
                record.add(root.val)
                dictionary[root.val].append(root)
                root = root.left
            else:
                # duplicate nodes are already in the set
                for every in dictionary[root.val]:
                    if tellSame(root, dictionary[root.val]):
                        answer.append(root.val)
            dictionary[root.val].append(root)
        else:
            root = stack.pop()
            root = root.right
    return answer

def tellSame(node1, node2):
    if not node1 and not node2:
        return True
    elif not node1 and node2:
        return False
    elif not node2 and node1:
        return False
    else:
        if node1.val != node2.val:
            return False
    return tellSame(node1.left, node2.left) and tellSame(node1.right, node2.right)
