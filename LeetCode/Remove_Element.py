class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Runtime: 36 ms, faster than 92.98% of Python3 online submissions for Remove Element.
        Memory Usage: 13.9 MB, less than 63.05% of Python3 online submissions for Remove Element.
        """
        for i in range(len(nums))[::-1]:
            if nums[i] == val:
                nums.pop(i) 
        return len(nums)