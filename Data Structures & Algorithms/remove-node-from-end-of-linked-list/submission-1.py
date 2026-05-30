# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        iter = head

        while iter:
            count += 1
            iter = iter.next
        
        index = count - n

        if index == 0:
            return head.next

        counter = 0

        tail = head
        prev = None
        while tail:
            if counter == index:
                prev.next = tail.next
            counter += 1
            prev = tail
            tail = tail.next


        return head