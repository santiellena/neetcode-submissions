class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
                # [ 1, 2, 3 ]
        #     
        #             .
        #      1      2       3
        #    2   3
        #    3   

        # I need some way to know the current state of a permutation
        result = []
        cur = []

        def dfs():
            if len(cur) == len(nums):
                result.append(cur.copy())
                return

            for n in nums:
                if n in cur:
                    continue

                cur.append(n)
                dfs()
                cur.pop()


            
        dfs()


        return result

