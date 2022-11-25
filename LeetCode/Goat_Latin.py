class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        """
        Runtime: 47 ms, faster than 72.35% of Python3 online submissions for Goat Latin.
        Memory Usage: 13.9 MB, less than 68.60% of Python3 online submissions for Goat Latin.
        """
        vowel = ["A","E","I","O","U","a","e","i","o","u"]
        goatlatin = []
        for ind, word in enumerate(sentence.split(" ")):
            if word[0] in vowel:
                word+="ma"
            else:
                word+=word[0]+"ma"
                word=word[1:]
            word+="a"*(ind+1)
            goatlatin.append(word)
        return " ".join(goatlatin)