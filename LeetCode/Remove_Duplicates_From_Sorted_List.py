# Leetcode 83
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from email import header
from wsgiref import headers


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    cur = head

    while cur:
            while cur.next and cur.next.val == cur.val:    # loop if next exists and cur val equals next val
                cur.next = cur.next.next
        cur = cur.next
    return head