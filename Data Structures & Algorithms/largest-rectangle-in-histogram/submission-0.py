class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            start = i

            while stack and stack[-1][0] > heights[i]:
                height, index = stack.pop()
                max_area = max(max_area, (i - index) * height)
                start = index

            stack.append((heights[i], start))

        for i in range(len(stack)):
            max_area = max(max_area, (len(heights) - stack[i][1]) * stack[i][0] )

        return max_area


