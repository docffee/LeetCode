class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        Runtime: 484 ms, faster than 97.13% of Python3 online submissions for Island Perimeter.
        Memory Usage: 14.1 MB, less than 93.38% of Python3 online submissions for Island Perimeter.
        """
        peri=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    peri+=4
                    if i>0 and grid[i-1][j] == 1:
                        peri-=2
                    if j>0 and grid[i][j-1] == 1:
                        peri-=2
        return peri