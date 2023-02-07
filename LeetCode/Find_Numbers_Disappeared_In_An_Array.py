class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """Runtime 347 ms Beats 82.36% Memory 29.3 MB Beats 7%"""
        f = set(nums)
        num = list(f)
                
                
        # print(num)
        a = len(nums)
        l = []
        k = []

        for i in range(1,len(nums)+1):
            l.append(i)
        d = list(set(l).difference(set(num)))
        return(d)