class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in list(seen.items()):
            bucket[value].append(key)

        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for j in range(len(bucket[i])):
                result.append(bucket[i][j])
                if len(result) == k:
                    return result






