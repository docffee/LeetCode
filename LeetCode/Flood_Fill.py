class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Runtime: 82 ms, faster than 89.40% of Python3 online submissions for Flood Fill.
        Memory Usage: 14.2 MB, less than 39.51% of Python3 online submissions for Flood Fill.
        """
        if image[sr][sc] == color:
            return image
        curColor = image[sr][sc]
        def dfs(row,col):
            if image[row][col] == curColor:
                image[row][col] = color
                if row >= 1:
                    dfs(row-1,col)
                if row+1 < len(image):
                    dfs(row+1,col)
                if col >=1:
                    dfs(row,col-1)
                if col+1 < len(image[0]):
                    dfs(row,col+1)
        dfs(sr,sc)    
        return image