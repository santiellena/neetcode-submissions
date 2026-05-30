class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        included = set()
        l = 0
        for r in range(len(s)):
            while s[r] in included:
                included.remove(s[l])
                l += 1

            included.add(s[r])

            longest = max(longest, len(included))

        return longest