class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Runtime: 38 ms 87.71% Memory Usage: 13.8 MB 98.50%
        return ''.join(word1) == ''.join(word2)