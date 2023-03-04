class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from typing import List
        stack = []
        mapping = {}
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                j = stack.pop()
                mapping[nums2[j]] = nums2[i]
            stack.append(i)
        return [mapping.get(elem, -1) for elem in nums1]