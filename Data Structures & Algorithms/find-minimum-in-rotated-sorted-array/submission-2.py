class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 1, len(nums)

        # binary search the amount of rotations:
        # [1,2,3,4,5,6] rot = 6
        # 
        # [3,4,5,6,1,2] rot = 5
        #  0       rot - n
        #  3         2
        # if nums[0] > nums[rot - n]:
        #   then rot is correct one or a smaller rot is

        rotations = float("inf")

        # O(log n)
        while l <= r:
            rot = (l + r) // 2

            if nums[0] >=  nums[rot - len(nums)]:
                rotations = min(rotations, rot)

                r = rot - 1
            else:
                l = rot + 1

        return nums[rotations % (len(nums))]


