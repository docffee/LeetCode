# LeetCode 206 Reverse Linked List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Reverse list iteratively by changing direction of pointers

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

#Reverse list recursively
    def reverseListRecursive(self, head):
        def rec(prev, cur):
            if not cur:
                return prev
            tail = rec(cur, cur.next)
            cur.next = prev
        return rec(None, head)