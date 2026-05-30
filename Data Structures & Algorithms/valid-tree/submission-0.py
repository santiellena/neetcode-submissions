class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = [[] for _ in range(n)]
        visited = set()

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(index: int, prev: int) -> bool:

            if index in visited:
                return False    

            visited.add(index)

            for n1 in adj[index]:
                if n1 != prev:
                    if not dfs(n1, index):
                        return False

            return True
        
        
        return dfs(0, -1) and len(visited) == n
