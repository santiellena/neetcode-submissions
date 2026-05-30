class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]


        def find(node) -> parent:

            while node != parents[node]:
                parents[node] = parents[parents[node]]
                node = parents[node]

            return node

        
        def union(n1, n2) -> int:
            n1 = find(n1)
            n2 = find(n2)

            if n1 == n2:
                return 0

            
            parents[n2] = parents[n1]

            return 1 
            



        for n1, n2 in edges:
            n -= union(n1, n2)

        return n