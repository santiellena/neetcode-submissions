class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_frequencies = {}
        s2_frequencies = {}

        for i in s1:
            s1_frequencies[i] = s1_frequencies.get(i, 0) + 1
        
        print(s1_frequencies)

        l = 0
        for r in range(len(s2)):
            s2_frequencies[s2[r]] = s2_frequencies.get(s2[r], 0) + 1

            while len(s1) < r - l + 1:
                s2_frequencies[s2[l]] = s2_frequencies.get(s2[l], 0) - 1
                if s2_frequencies[s2[l]] == 0:
                    del s2_frequencies[s2[l]]
                l += 1
            
            if s1_frequencies == s2_frequencies:
                return True
        
        return False
        