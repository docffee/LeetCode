class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """
        Runtime: 65 ms, faster than 25.00% of Python3 online submissions for Path Crossing.
        Memory Usage: 14 MB, less than 27.02% of Python3 online submissions for Path Crossing.
        """
        visited = [(0,0)]
        compass = {"N":[0,1],"S":[0,-1],"E":[1,0],"W":[-1,0]}
        for i in path:
            x,y=visited[-1]
            x+=compass[i][0]
            y+=compass[i][1]
            if (x,y) in visited:
                return True
            visited.append((x,y))
        return False
