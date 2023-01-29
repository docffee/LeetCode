class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        """Runtime 63 ms Beats 85.22% Memory 14.1 MB Beats 48.85%"""
        while original > 0:   
            tmp = original
            if original in nums:
                nums.pop(nums.index(tmp))
            else:
                return original
            original = original*2
            