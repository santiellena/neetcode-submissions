class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        sorted_s1 = "".join(sorted(s1))
        for r in range(len(s2)):
            while len(s1) < r - l + 1:
                l += 1
            else: # they equal in lenght
                if sorted_s1 == "".join(sorted(s2[l:(r + 1)])):
                    return True
            
        return False