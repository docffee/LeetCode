class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """Runtime: 44 ms, faster than 92.05% of Python3 online submissions for Baseball Game.
        Memory Usage: 14.2 MB, less than 32.76% of Python3 online submissions for Baseball Game."""
        arr = []
        for i in operations:
            if i.lstrip('-').isdigit():
                arr.append(int(i))
            elif i == '+':
                arr.append(int(arr[-1])+int(arr[-2]))
            elif i == 'D':
                arr.append(2*int(arr[-1]))
            elif i == 'C':
                arr.pop(-1)
        return sum(arr)