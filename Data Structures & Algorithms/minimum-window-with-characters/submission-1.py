class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minimum = ""
        l = 0
        count_t = {}
        count_s = {}
        for i in t:
            count_t[i] = count_t.get(i, 0) + 1
        
        count_t_list = list(count_t.items())

        for r in range(len(s)):
            count_s[s[r]] = count_s.get(s[r], 0) + 1

            window_includes_chars = True
            for char, freq in count_t_list:
                if count_s.get(char, 0) < freq:
                    window_includes_chars = False
                    break

            while window_includes_chars:
                if minimum == "":
                    minimum = s[l:r + 1]
                elif len(minimum) > len(s[l:r + 1]):
                    minimum = s[l:r + 1]

                
                
                count_s[s[l]] = count_s.get(s[l], 0) - 1
                if count_t.get(s[l], 0) > count_s.get(s[l], 0):
                    window_includes_chars = False
                l += 1


        return minimum


        


