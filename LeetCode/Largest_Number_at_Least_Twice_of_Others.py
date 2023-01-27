class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        """Runtime 50 ms Beats 34.17% Memory 14 MB Beats 9.41%"""
        i=nums.index(max(nums))
        m=max(nums)
        nums.pop(i)
        j=nums.index(max(nums))
        if m >= 2*nums[j]:
            return i
        return -1