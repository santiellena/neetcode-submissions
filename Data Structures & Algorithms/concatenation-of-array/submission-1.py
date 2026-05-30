class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_vec = []
        nums_lenght = len(nums)

        if nums_lenght == 0 or nums_lenght > 1000:
            return []

        for i in range(2 * nums_lenght):
            value = nums[i % nums_lenght]
            if i < nums_lenght:
                if value < 1 or value > 1000:
                    return []
            
            new_vec.append(value)
        
        return new_vec
        