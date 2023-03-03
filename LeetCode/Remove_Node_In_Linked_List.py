# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(pre):
            cur = pre.next
            if not cur.next:
                return cur.val
            cur_max = dfs(cur) 
            if cur_max > cur.val:
                pre.next = cur.next
            return max(cur_max, cur.val)
        new_head = ListNode()
        new_head.next = head
        dfs(new_head)
        return new_head.next
                
        