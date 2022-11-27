# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Runtime: 33 ms, faster than 91.51% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.9 MB, less than 59.95% of Python3 online submissions for Binary Tree Inorder Traversal.
"""

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # inorder: left -> root -> right
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return res

"""
Runtime: 69 ms, faster than 8.34% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.8 MB, less than 97.07% of Python3 online submissions for Binary Tree Inorder Traversal.
"""
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        return res