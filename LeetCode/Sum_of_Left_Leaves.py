# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Runtime: 72 ms, faster than 17.14% of Python3 online submissions for Sum of Left Leaves.
    Memory Usage: 14.2 MB, less than 90.43% of Python3 online submissions for Sum of Left Leaves.
    """
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        while root:
            if root.left:
                pre, isLeft = root.left, True
                while pre.right and pre.right != root:
                    pre = pre.right
                if not pre.right:
                    pre.right = root
                    root = root.left
                else:
                    pre.right = None
                    if pre == root.left and not pre.left:
                        ans = ans + pre.val
                    root = root.right
            else:
                root = root.right
        return ans