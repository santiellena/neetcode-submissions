# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        tail = head
        counter = 0

        while tail:
            counter += 1
            tail = tail.next

        middle = counter // 2 

        prev = None
        curr = head
        # reversing the list from the middle to the end
        # so in the end, prev si the tail of the initial linked list
        # but the head of my second list
        while curr:
            if middle == counter - 1:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            else:
                curr = curr.next
                counter -= 1


        # 1) 1 -> 2 -> 3
        # 2) 5 -> 4

        while prev and head:
            h_nxt = head.next
            head.next = prev
            p_nxt = prev.next
            prev.next = h_nxt
            prev = p_nxt
            head = h_nxt

        




