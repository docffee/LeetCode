# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Runtime: 59 ms, faster than 40.58% of Python3 online submissions for Binary Tree Preorder Traversal.
        Memory Usage: 13.8 MB, less than 96.78% of Python3 online submissions for Binary Tree Preorder Traversal.
        """
        if root is None:
            return []
        list1 = []
        def dfs(node, list1):
            if node is None:
                return list1
            list1.append(node.val)
            dfs(node.left, list1)
            dfs(node.right, list1)
            return list1
        return dfs(root,list1)
        