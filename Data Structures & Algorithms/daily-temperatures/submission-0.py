class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                result[stack[-1][1]] = i - stack[-1][1] 
                stack.pop()

            stack.append((temperatures[i], i))

        return result
