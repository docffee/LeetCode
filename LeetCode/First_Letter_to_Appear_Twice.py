class Solution:
    def repeatedCharacter(self, s: str) -> str:
        """Runtime 46 ms Beats 32.45% Memory 13.9 MB Beats 46.56%"""
        dicta={}
        for i in s:
            if i in dicta:
                return i
            else:
                dicta[i]=1