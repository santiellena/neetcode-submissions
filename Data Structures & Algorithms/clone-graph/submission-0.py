"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldToNewNode = {}
        # first pass to create new nodes
        def first_dfs(node: Node):
            oldToNewNode[node] = Node(node.val)
            
            if node.neighbors: 
                for neighbor in node.neighbors:
                    if neighbor not in oldToNewNode:
                        first_dfs(neighbor)            
        
        first_dfs(node)

        seen = set()
        def second_dfs(node: Node):

            newNode = oldToNewNode[node]

            if node not in seen:
                seen.add(node)
                if node.neighbors: 
                    for neighbor in node.neighbors:
                        newNode.neighbors.append(oldToNewNode[neighbor])
                        if neighbor not in seen:
                            second_dfs(neighbor)   

        
        second_dfs(node)
        # second pass to link nodes

        return oldToNewNode[node]

