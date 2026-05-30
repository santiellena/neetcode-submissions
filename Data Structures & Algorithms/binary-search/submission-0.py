class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, u = 0, len(nums) - 1

        while l <= u:
            mid_index = ( l + u ) // 2
            if target == nums[mid_index]:
                return mid_index
            elif target > nums[mid_index]:
                l = mid_index + 1
            else:
                u = mid_index - 1

        return -1 