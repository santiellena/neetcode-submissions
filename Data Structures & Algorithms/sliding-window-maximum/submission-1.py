
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        curr_max = -11000
        curr_max_i = -1
        max_windows = []
        for r in range(len(nums)):
            if k == r - l + 1:
                # move to right both pointers and update max
                if l - 1 == curr_max_i:
                    l_i = l
                    curr_max_i = -1
                    curr_max = -11000
                    while l_i <= r:
                        if curr_max < nums[l_i]:
                            curr_max = nums[l_i]
                            curr_max_i = l_i
                        l_i += 1
                    
                elif nums[r] > curr_max:
                    curr_max = nums[r]
                    curr_max_i = r

                max_windows.append(curr_max)
                

                l += 1
            else: 
                if curr_max < nums[r]:
                    curr_max = nums[r]
                    curr_max_i = r
                

        return max_windows