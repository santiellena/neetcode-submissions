class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # [1, 2, 3]

        #           .
        #        _     1
        #      _   2  _  2
        #     _ 3 _ 3 _3 _ 3
        self.sets = []
        self.subset = []
        def dfs(i: int):
            if i == len(nums):
                self.sets.append(self.subset.copy())
                return 


            self.subset.append(nums[i])
            include = dfs(i+1) # include

            self.subset.pop()
            not_include = dfs(i+1) # not include

        
            return

        dfs(0)
            

        return self.sets