class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """Runtime 133 ms Beats 85.60% Memory 15.8 MB Beats 6.98%"""
        vals = set(nums)
        for i in range(len(nums)+1):
            if i not in vals:
                return i