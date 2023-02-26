class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        from typing import Counter
        l = len(nums)
        c = Counter(nums)
        for i in c:
            if(c[i] >= 2):
                return i