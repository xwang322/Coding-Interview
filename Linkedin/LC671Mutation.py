'''
利特抠留齐腰，follow up 是 find 3rd minimum or kth minimum value。这个磨磨唧唧弄了半天想改下之前的代码，想在dfs加个counter结果发现不对。
和里特扣而伞林也不一样，因为那题是b s t。只好说用bfs把node扫一遍找第k小。然后天竺大爷就说move on next question了。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root, k):
        if not root:
            return -1
        heap = []
        queue = [root]
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if len(heap) < k:
                    heapq.heappush(heap, node.val)
                else:
                    heapq.heapreplace(heap, node.val)
                if node.left and node.right:
                    queue.append(node.left)
                    queue.append(node.right)
        if len(heap) < k:
            return -1
        while heap:
            answer = heap.pop()
        return answer
