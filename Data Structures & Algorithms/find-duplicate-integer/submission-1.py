class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        # [ 3  1  2  3 ]
        # [ 2          ]
        i = 0
        while i <= len(nums):
            
            if nums[i] == i + 1:
                i += 1
            else:
                tmp = nums[nums[i] - 1]
                
                if tmp == nums[i]:
                    return tmp

                nums[nums[i] - 1] = nums[i]
                nums[i] = tmp

            
        return i


            

        
