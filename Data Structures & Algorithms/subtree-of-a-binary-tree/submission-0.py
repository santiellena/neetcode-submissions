# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def areEqual(p: Optional[TreeNode], q: Optional[TreeNode]):
            if p is None or q is None:
                if p is None and q is None:
                    return True
            if q and p:
                left = areEqual(p.left, q.left)
                right = areEqual(p.right, q.right)

                return left and right and p.val == q.val

            return False

        if not subRoot:
            return True

        if not root:
            return False

        if areEqual(root, subRoot):
            return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right

            
            

        