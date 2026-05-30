class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        relation = {}
        relation["["] = "]"
        relation["("] = ")"
        relation["{"] = "}"

        if len(s) % 2 != 0:
            return False

        for i in s:
            if i in relation:
                stack.append(i)
            else:
                if stack and relation[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        

        return len(stack) == 0