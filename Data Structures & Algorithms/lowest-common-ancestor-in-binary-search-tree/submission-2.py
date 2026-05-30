# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def binSearchPath(root: TreeNode, node: TreeNode) -> List[TreeNode]:
            stack = [root]

            while root.val != node.val:
                if not root.left:
                    stack.append(root.right)
                    root = root.right

                elif not root.right:
                    stack.append(root.left)
                    root = root.left
                
                else:
                    if node.val > root.val:
                        stack.append(root.right)
                        root = root.right
                    else:
                        stack.append(root.left)
                        root = root.left


            return stack

        p_root = root
        q_root = root
        
        stack_p = binSearchPath(p_root, p)
        stack_q = binSearchPath(q_root, q)

        print(stack_p)
        print(stack_q)

        while True:
            if len(stack_p) > len(stack_q):
                stack_p.pop()
            elif len(stack_p) < len(stack_q):
                stack_q.pop()
            else:
                q_pop = stack_q.pop()
                p_pop = stack_p.pop()

                if q_pop == p_pop:
                    return q_pop









