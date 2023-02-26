class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        """
        Runtime: 48 ms, faster than 77.72% of Python3 online submissions for Determine if String Halves Are Alike.
        Memory Usage: 13.9 MB, less than 77.72% of Python3 online submissions for Determine if String Halves Are Alike.
        """
        a,b = 0,0
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(int(len(s)/2)):
            if s[i] in vowel:
                a+=1
            if s[-i-1] in vowel:
                b+=1
        return a == b
                