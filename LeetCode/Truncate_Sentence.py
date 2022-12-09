class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        """
        Runtime: 37 ms, faster than 85.33% of Python3 online submissions for Truncate Sentence.
        Memory Usage: 13.8 MB, less than 61.72% of Python3 online submissions for Truncate Sentence.
        """
        return " ".join(list(s.split(" "))[0:k])
