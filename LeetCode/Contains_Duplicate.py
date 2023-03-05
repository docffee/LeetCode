class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        test = {}
        for n in nums:
            if n in test:
                return True
            else:
                test[n] = 1
        return False