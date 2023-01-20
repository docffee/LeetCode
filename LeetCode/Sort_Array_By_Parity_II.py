class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """Runtime 207 ms Beats 89.51% Memory 16.7 MB Beats 19.27%"""
        ans=[]
        even = [n for n in nums if n%2 == 0]
        odd =  [n for n in nums if n%2 == 1]
        for a, b in zip(even, odd):
            ans.append(a)
            ans.append(b)
        return ans