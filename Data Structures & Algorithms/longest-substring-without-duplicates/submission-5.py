class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        l, r = 0, 1
        seen = {}
        seen[s[l]] = 0

        longest = 1

        while r < len(s):
            if seen.get(s[r], -1) == -1:
                seen[s[r]] = r
                longest = max(longest, r - l + 1)
                r += 1
            else:
                l = seen.get(s[r], -1) + 1
                r = l + 1
                seen = {}
                seen[s[l]] = l
        
        return longest
                



