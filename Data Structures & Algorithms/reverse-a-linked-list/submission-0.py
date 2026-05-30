# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(pre: Optional[ListNode], pos: ListNode) -> ListNode:
            if pos.next is not None:
                new_head = reverse(pos, pos.next)
            else:
                new_head = pos

            pos.next = pre
            return new_head
           

        if head == None:
            return None

        return reverse(None, head)


        