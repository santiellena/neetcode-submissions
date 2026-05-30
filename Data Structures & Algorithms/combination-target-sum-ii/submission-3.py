class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def dfs(index: int, path: List[int], total: int) -> None:
            #               .
            #           1       _
            #         2   _   2   _
            #        3 _ 3 _ 3 _ 3 _

            if total == target:
                result.append(path.copy())
                return

            if index >= len(candidates) or total > target:
                return

            
            path.append(candidates[index])
            dfs(index + 1, path, total + candidates[index]) # include path

            path.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1

            dfs(index + 1, path, total) # not include path


        dfs(0, [], 0)

        return result