# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head
        counter = 0
        while counter != n:
            right = right.next
            counter += 1

        prev = None
        while right:
            right = right.next
            prev = left
            left = left.next
        
        if prev == None:
            head = head.next
        else:
            prev.next = left.next

        return head