# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goods = 0

        def dfs(node: TreeNode, biggest: int):
            if not node:
                return None


            if node.val >= biggest:
                self.goods += 1

            dfs(node.left, max(biggest, node.val))
            dfs(node.right, max(biggest, node.val))

            return None

        dfs(root, root.val)

        return self.goods