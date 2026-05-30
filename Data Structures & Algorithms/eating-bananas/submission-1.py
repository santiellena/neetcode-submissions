class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        best = float("inf")
        l, r = 1, max(piles)
        while l <= r:
            k = (l + r) // 2
            hours_taken = 0
            for pile in piles:
                hours_taken += math.ceil(pile / k)

            if hours_taken <= h:
                best = min(best, k)

                r = k - 1
            else:
                l = k + 1
        
        return best
        