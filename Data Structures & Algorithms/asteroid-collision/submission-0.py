class Solution:
    def collide(self, stack: List[int]) -> List[int]:
        if len(stack) >= 2:
            if stack[-1] < 0 and stack[-2] > 0:
                if abs(stack[-1]) > stack[-2]:
                    kept = stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(kept)
                elif abs(stack[-1]) < stack[-2]:
                    stack.pop()
                else:
                    stack.pop()
                    stack.pop()

                stack = self.collide(stack)

        return stack

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            stack.append(asteroid)

            stack = self.collide(stack)
            
        return stack