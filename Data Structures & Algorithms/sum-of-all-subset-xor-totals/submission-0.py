class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0

        def dfs(i, total) -> int:
            if i == len(nums):
                return total

            not_include_branch = dfs(i + 1, total) # not include
            include_branch = dfs(i + 1, total ^ nums[i]) # include

            return not_include_branch + include_branch
        return dfs(0, 0)