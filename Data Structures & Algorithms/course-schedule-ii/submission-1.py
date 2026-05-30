class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = [0 for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            degree[course] += 1

        dq =  collections.deque()
        
        for course in range(len(degree)):
            if degree[course] == 0:
                dq.append(course)

        order = []
        while dq:
            course = dq.popleft()

            order.append(course)

            for crs, pre in prerequisites:
                if pre == course:
                    degree[crs] -= 1
                    if degree[crs] == 0:
                        dq.append(crs)

        if len(order) == numCourses:
            return order
        else:
            return []

        
        
