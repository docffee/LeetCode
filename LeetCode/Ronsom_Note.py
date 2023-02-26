class Solution:
    def canConstruct(self, ransomNote, magazine):
        """Runtime 63 ms Beats 67.36% Memory 14.2 MB Beats 49.78%"""
        for letter in set(ransomNote):
            if magazine.count(letter) < ransomNote.count(letter):
                return False
        return True