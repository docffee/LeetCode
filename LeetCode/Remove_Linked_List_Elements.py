# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """Runtime 68 ms Beats 79.50% Memory 17.7 MB Beats 93.10%"""
        while head and head.val == val:
            head = head.next
        current = head

        while current:
            while current and current.next and current.next.val == val:
                current.next = current.next.next
            current = current.next
        return head