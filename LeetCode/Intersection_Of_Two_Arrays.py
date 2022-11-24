class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Runtime: 41 ms, faster than 98.86% of Python3 online submissions for Intersection of Two Arrays.
        Memory Usage: 14.2 MB, less than 25.48% of Python3 online submissions for Intersection of Two Arrays."""
        return list(set(nums1).intersection(set(nums2)))