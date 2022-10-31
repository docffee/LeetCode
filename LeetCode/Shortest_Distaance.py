class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        """Runtime: Runtime: 69 ms, faster than 94.07% of Python3 online submissions for Shortest Word Distance.
        Memory Usage: 17.7 MB, less than 48.04% of Python3 online submissions for Shortest Word Distance."""
        mindist = len(wordsDict)
        ind1, ind2 = -1, -1
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                ind1 = i
            if wordsDict[i] == word2:
                ind2 = i
            if ind1 != -1 and ind2 != -1 and abs(ind1-ind2) < mindist:
                mindist = abs(ind2-ind1)
        return mindist

    def shortestDistanceBrute(self, wordsDict: List[str], word1: str, word2: str) -> int:
        """Runtime: 80 ms, faster than 81.32% of Python3 online submissions for Shortest Word Distance.
        Memory Usage: 17.8 MB, less than 48.04% of Python3 online submissions for Shortest Word Distance."""
        mindist = len(wordsDict)
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1 
                for j in range(len(wordsDict)):
                    if wordsDict[j] == word2:
                        dist = abs(i - j)
                        if dist < mindist:
                                mindist = dist
        return mindist
