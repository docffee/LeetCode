# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Runtime: 41 ms, faster than 79.50% of Python3 online submissions for Same Tree.
Memory Usage: 13.9 MB, less than 29.69% of Python3 online submissions for Same Tree.
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right))