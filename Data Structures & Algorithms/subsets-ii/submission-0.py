class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def dfs(i: int, path: List[int]) -> None:
            if i == len(nums):
                result.append(path.copy())
                return None

            path.append(nums[i])
            dfs(i + 1, path)

            path.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1, path)


        dfs(0, [])

        return result