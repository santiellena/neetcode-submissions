# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")

        def dfs(root) -> int: 
            if not root:
                return 0
        
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))

            self.res = max(self.res, root.val + right + left)
            return max(root.val + left, root.val + right)

        max_path = dfs(root)
        return max(self.res, max_path)