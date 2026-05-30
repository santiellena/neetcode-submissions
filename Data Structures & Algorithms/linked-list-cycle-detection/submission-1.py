# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tail = head
        slow_tail = head

        counter = 0
        while tail:
            if tail == slow_tail and counter != 0:
                return True
            else:
                if counter % 2 != 0:
                    slow_tail = slow_tail.next
                tail = tail.next
                counter += 1

        return False
                

