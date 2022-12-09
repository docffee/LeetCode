class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        """
        Runtime: 65 ms, faster than 83.25% of Python3 online submissions for Shuffle String.
        Memory Usage: 13.9 MB, less than 63.76% of Python3 online submissions for Shuffle String.
        """
        s1 = str()
        for i in range(len(s)):
            s1+=s[indices.index(i)]
        return s1