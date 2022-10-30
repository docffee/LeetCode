class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """Runtime: 197 ms, faster than 78.21% of Python3 online submissions for Single Number.
        Memory Usage: 16.7 MB, less than 49.96% of Python3 online submissions for Single Number."""
        asdf = {}
        for i in nums:
            if i not in asdf:
                asdf[i] = 1
            else:
                asdf[i] +=1
        for i in asdf:
            if asdf[i] == 1:
                return i