# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        h=0
        if not root:
            return 0
        def height(node):
            if not node:
                return 0
            left=height(node.left)# left subtree height
            right=height(node.right) # right subtree height
            if left>right:
                h=1+left
            else:
                h=1+right
            return h
        leftheight=height(root.left)#0
        rightheight=height(root.right)#0
        ldiameter=self.diameterOfBinaryTree(root.left)#0
        rdiameter=self.diameterOfBinaryTree(root.right)#0
        return max(leftheight+rightheight,max(ldiameter,rdiameter))