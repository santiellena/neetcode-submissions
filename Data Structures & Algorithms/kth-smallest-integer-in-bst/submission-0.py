# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.heap = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return None

            heapq.heappush(self.heap, -node.val)

            while len(self.heap) > k:
                heapq.heappop(self.heap)
            
            dfs(node.left)
            dfs(node.right)
            return None

        dfs(root)

        return -(heapq.heappop(self.heap))
