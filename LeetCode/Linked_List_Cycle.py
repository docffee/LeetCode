# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Runtime: 78 ms 77.09% Memory Usage: 17.7 MB 31.18%
        # turtle and hare approache
        turtle, hare = head, head
        while hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next 
            if turtle == hare:
                return True
        return False