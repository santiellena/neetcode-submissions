class Solution:
    def trap(self, height: List[int]) -> int:

        max_l_at = []
        max_r_at = [0 for _ in range(len(height))]

        last_max_l = 0
        for i in range(len(height)):
            max_l_at.append(last_max_l)
            if last_max_l < height[i]:
                last_max_l = height[i]

        last_max_r = 0
        for r in range(len(height) - 1, -1, -1):
            max_r_at[r] = last_max_r
            print(r)
            if last_max_r < height[r]:
                last_max_r = height[r]

        area = 0
        for i in range(len(height)):

            area += max(0, min(max_l_at[i], max_r_at[i]) - height[i])
        
        return area
            