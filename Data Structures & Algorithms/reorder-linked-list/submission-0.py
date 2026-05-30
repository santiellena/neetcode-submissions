# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def printList(self, head: ListNode) -> None:
        output = ""
        iter = head
        while iter:
            output.join(str(iter.val))
            output.join("-->")
            iter = iter.next

        print(output)

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        # find start of second half
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # slow now is the first node of the 2nd half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt


        # now prev is the tail of my initial list but with the directions reversed
        tail = prev
        counter = 0
        dummy = ListNode()
        while tail and head:
            if counter % 2 == 0:
                dummy.next = head
                head = head.next
            else:
                dummy.next = tail
                tail = tail.next
            dummy = dummy.next    
            counter += 1

        






