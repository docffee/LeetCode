class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """Runtime 89 ms Beats 63.31% Memory 14.6 MB Beats 96.16%"""
        evens=[]
        odds=[]
        for ele in nums:
            if ele%2==0:
                evens.append(ele)
            else:
                odds.append(ele)
        return evens+odds