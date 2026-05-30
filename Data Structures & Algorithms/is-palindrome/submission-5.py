class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for i in list(s.lower()):
            if i.isalnum():
                s_list.append(i)
        s2 = s_list.copy()
        s_list.reverse()
        return s_list == s2   

      