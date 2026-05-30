class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i + 1 for i in range(n)]
        result = []

        def dfs(index: int, path: List[int]):
            if len(path) == k:
                result.append(path.copy())
                return
            if index == len(nums):
                return
            
            path.append(nums[index])
            dfs(index + 1, path)

            path.pop()
            dfs(index + 1, path)


        dfs(0, [])

        return result