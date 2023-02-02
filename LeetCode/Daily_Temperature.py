class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """Runtime 1438 ms Beats 77.20% Memory 30.7 MB Beats 7.96%"""
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res