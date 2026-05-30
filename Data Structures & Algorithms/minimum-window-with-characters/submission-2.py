class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minimum = ""
        l = 0
        count_t = {}
        count_s = {}
        have = 0
        for i in t:
            count_t[i] = count_t.get(i, 0) + 1
        
        need = len(count_t.keys())

        for r in range(len(s)):
            count_s[s[r]] = count_s.get(s[r], 0) + 1

            if count_t.get(s[r], 0) == count_s.get(s[r], 0):
                have += 1

            while have == need:
                if minimum == "":
                    minimum = s[l:r + 1]
                elif len(minimum) > len(s[l:r + 1]):
                    minimum = s[l:r + 1]
                
                count_s[s[l]] = count_s.get(s[l], 0) - 1
                if count_t.get(s[l], 0) > count_s.get(s[l], 0):
                    have -= 1
                l += 1


        return minimum


        


