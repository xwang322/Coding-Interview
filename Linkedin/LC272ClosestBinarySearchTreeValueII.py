# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        heap = []
        self.dfs(root, target, k , heap)
        answer = []
        while heap:
            answer.append(heapq.heappop(heap)[1])
        return answer

    def dfs(self, root, target, k, heap):
        if not root:
            return
        heapq.heappush(heap, (-abs(root.val - target), root.val))
        self.dfs(root.left, target, k, heap)
        self.dfs(root.right, target, k, heap)
        if len(heap) > k:
            heapq.heappop(heap)
