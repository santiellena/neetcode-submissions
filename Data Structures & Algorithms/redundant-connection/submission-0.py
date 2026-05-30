class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        parents = [i for i in range(n)]
        ranks = [1] * n

        cycles = []

        def find(node):
            while node != parents[node]:
                parents[node] = parents[parents[node]]
                node = parents[node]

            return node             

        
        def union(n1, n2) -> bool:
            n1 = find(n1)
            n2 = find(n2)

            if n1 == n2:
                return False

            if ranks[n1] > ranks[n2]:
                parents[n2] = n1
                ranks[n1] += ranks[n2]
            elif ranks[n2] > ranks[n1]:
                parents[n1] = n2
                ranks[n2] += ranks[n1]
            else:
                parents[n2] = n1
                ranks[n1] += 1

            return True


        for n1, n2 in edges:
            print(parents)
            if not union(n1, n2):
                cycles.append([n1, n2])

        return cycles[-1]