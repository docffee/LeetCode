class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """Runtime 57 ms Beats 76.17 %Memory 13.8 MB Beats 85.80%"""
        hs=set()
        for num in arr:
            if num/2 in hs or num*2 in hs:
                return True
            else:
                hs.add(num)
        return False