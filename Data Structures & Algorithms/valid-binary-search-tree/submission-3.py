# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(root: Optional[TreeNode], smaller: int, greater: int) -> bool:
            if not root:
                return True

            if not (root.val > smaller and root.val < greater):
                return False
            
            left = dfs(root.left, smaller, root.val)
            right = dfs(root.right, root.val, greater)
            

            return left and right

        
        return dfs(root, float("-inf"), float("inf"))