# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        def dfs(node):
            if not node.left and node.right:
                values.append(node.right.val)
            if not node.right and node.left:
                values.append(node.left.val)
            
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return values