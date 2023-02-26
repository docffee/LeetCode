class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Runtime: 41 ms, faster than 98.86% of Python3 online submissions for Intersection of Two Arrays.
        Memory Usage: 14.2 MB, less than 25.48% of Python3 online submissions for Intersection of Two Arrays."""
        return list(set(nums1).intersection(set(nums2)))

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Runtime: 72 ms, faster than 76.86% of Python3 online submissions for Intersection of Two Arrays.
        Memory Usage: 14 MB, less than 68.92% of Python3 online submissions for Intersection of Two Arrays.
        """
        ans=[]
        for i in nums1:
            if i in nums2:
                ans.append(i)
        return list(set(ans))

    def intersection3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Runtime: 122 ms, faster than 20.23% of Python3 online submissions for Intersection of Two Arrays.
        Memory Usage: 14 MB, less than 91.71% of Python3 online submissions for Intersection of Two Arrays.
        """
        ans={}
        for i in nums1:
            if i in nums2:
                ans[i] = 1
        return list(set(ans))