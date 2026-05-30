class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        inDegree = [0 for _ in range(numCourses)]

        for course, prereq in prerequisites:
            inDegree[course] += 1

        dq = collections.deque()

        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                dq.append(i)

        index = 0
        order = [0 for _ in range(numCourses)]

        while dq:
            at = dq.popleft()
            order[index] = at
            index += 1
            # Substract a degree from those who have one from "at"
            # and add them to the deque if degree = 0
            for course, prereq in prerequisites:
                if at == prereq: 
                    inDegree[course] -= 1
                    if inDegree[course] == 0:
                        dq.append(course)

        if index != numCourses:
            return False
        else:
            return True

            