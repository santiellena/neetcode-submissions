class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l, m, r = 0, 1, len(nums) - 1
        nums.sort()

        triplets = []
        seen = set()
        while m < r:
            
            target = nums[l] * (-1)

            while m < r:
                res = nums[m] + nums[r]
                if res == target:
                    triplet = [nums[l], nums[m], nums[r]]
                    if tuple(triplet) not in seen:
                        triplets.append(triplet)
                        seen.add(tuple(triplet))

                    m += 1
                elif res < target:
                    m += 1
                else:
                    r -= 1


            l += 1
            m, r = l + 1, len(nums) - 1

        return triplets



