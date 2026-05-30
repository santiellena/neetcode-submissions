class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # how much time it takes to arrive at the target?
        # if a car is faster than the one next to it, then they become a fleet

        # [ (pos, speed, time_taken), ... ]
        #       car

        # target = 10
        # [ (2, 4, 2),  ] -> (4, 4, 1.25)

        # [ (2, 4, 2), (4, 4, 1.25) ]

        # (target - position) / speed = time it takes for a car to get to target

        stack = []
        cars = []

        for i in range(len(speed)):
            # pos, time_to_target
            cars.append((position[i], (target - position[i]) / speed[i]))
        
        cars.sort()

        for position, time in cars:
            while stack and stack[-1][1] <= time:
                stack.pop()
            stack.append((position, time))

        return len(stack)
