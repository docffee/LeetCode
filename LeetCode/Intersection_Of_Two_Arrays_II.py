class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Runtime: 170 ms, faster than 9.00% of Python3 online submissions for Intersection of Two Arrays II.
        Memory Usage: 13.9 MB, less than 85.55% of Python3 online submissions for Intersection of Two Arrays II.
        """
        res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    res.append(nums1[i])
                    nums2[j] = None
                    break
        return res