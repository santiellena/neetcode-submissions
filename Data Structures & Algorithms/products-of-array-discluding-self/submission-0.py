class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []

        for num in nums:
            if not prefix:
                prefix.append(num)
            else:
                prefix.append(num * prefix[-1])
        nums1 = nums.copy()
        nums1.reverse()
        for num in nums1:
            if not postfix:
                postfix.append(num)
            else:
                postfix.append(num * postfix[-1])

        postfix.reverse()
        
        result = []

        for i in range(len(prefix)):
            if i == 0:
                result.append(postfix[i + 1])
            elif i == len(prefix) - 1:
                result.append(prefix[i - 1])
            else:
                result.append(prefix[i - 1] * postfix[i + 1])

        return result        

