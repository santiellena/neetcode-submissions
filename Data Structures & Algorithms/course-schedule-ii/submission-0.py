class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = [0 for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            degree[course] += 1

        dq =  collections.deque()
        
        for course in range(len(degree)):
            if degree[course] == 0:
                dq.append(course)

        index = 0
        order = [0 for _ in range(numCourses)]
        while dq:
            course = dq.popleft()

            order[index] = course
            index += 1

            for crs, pre in prerequisites:
                if pre == course:
                    degree[crs] -= 1
                    if degree[crs] == 0:
                        dq.append(crs)

        if index == numCourses:
            return order
        else:
            return []

        
        
