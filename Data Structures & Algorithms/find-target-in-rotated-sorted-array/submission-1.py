class Solution:
    def search(self, nums: List[int], target: int) -> int:
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

        
        # to find an element in the rotated list
        # nums[(i + rotations) % len(nums)]
        # so, binary search shifting arrays

        # O(log n)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[(mid + rotations) % len(nums)] == target:
                print
                return ((mid + rotations) % len(nums))
            elif nums[(mid + rotations) % len(nums)] > target:
                r = mid - 1
            else:
                l = mid + 1


        return -1
        


