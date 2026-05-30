"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        tail = head
        while tail:
            copy = Node(tail.val)
            oldToCopy[tail] = copy

            tail = tail.next

        tail = head
        while tail:
            copy = oldToCopy[tail]
            copy.next = oldToCopy[tail.next]
            copy.random = oldToCopy[tail.random]

            tail = tail.next


        return oldToCopy[head]
        


        
