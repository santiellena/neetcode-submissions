class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0 
    
        for r in range(k - 1, len(arr)):
            if r + 1 < len(arr) and abs(arr[l] - x) > abs(arr[r + 1] - x) or r + 1 < len(arr) and arr[l] == arr[r + 1]:
                l += 1
            else:
                return arr[l:r + 1]
        

            