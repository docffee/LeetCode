    def tree2str(self, root: Optional[TreeNode]) -> str:
                    
        if(root == None):
            return ""
        
        output: str = str(root.val)
        
        if (root.left != None or root.right != None):
            output += "(" + self.tree2str(root.left) + ")"
            
        if (root.right != None):
            output += "(" + self.tree2str(root.right) + ")"          
        
        return output
