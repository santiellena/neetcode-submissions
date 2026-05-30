class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        for i in range(len(height)):
            max_l, max_r = 0, 0
            l, r = 0, len(height) - 1

            while l < i:
                if max_l < height[l]:
                    max_l = height[l]
                l += 1

            while r > i:
                if max_r < height[r]:
                    max_r = height[r]
                r -= 1

            area += max(0, min(max_l, max_r) - height[i])
        
        return area
            