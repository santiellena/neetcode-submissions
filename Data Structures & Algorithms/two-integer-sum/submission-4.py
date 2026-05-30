class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            rest = target - nums[i]

            rest_i = seen.get(rest, -1)

            if rest_i != -1 and rest_i != i:
                return [rest_i, i]

            seen[nums[i]] = i
            