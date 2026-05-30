class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            lh = heights[l]
            rh = heights[r]
            new_area = min(lh, rh) * (r - l)

            if new_area > area:
                area = new_area

            if lh > rh:
                r -= 1
            else: 
                l += 1

        return area