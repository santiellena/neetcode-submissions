class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for i in list(s.lower()):
            if i.isalnum():
                s_list.append(i)
        
        left = 0
        right = len(s_list) - 1

        while left < right:
            if s_list[left] != s_list[right]:
                return False

            left += 1
            right -= 1

        return True      

      