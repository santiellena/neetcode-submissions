class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        #       
        #    [ 1, 2, 3 ]
        #            _
        #            .
        #       1          _ 
        #    2    _      2   _ 
        #   3 _  3 _    3 _ 3 _
        #    
        # [], [2, 3], [3]


        def dfs(index: int, total: int):
            if index >= len(nums):
                return total

            return (dfs(index + 1, total ^ nums[index]) + dfs(index + 1, total))


        return dfs(0, 0)

        