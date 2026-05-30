class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0 for _ in range(len(temperatures))]

        for i, temperature in enumerate(temperatures):
            
            while stack and stack[-1][1] < temperature:
                old_i, old_temp = stack.pop()

                results[old_i] = i - old_i

            stack.append([i, temperature])

        return results
