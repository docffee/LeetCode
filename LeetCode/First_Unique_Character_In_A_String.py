class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Runtime: 215 ms, faster than 60.57% of Python3 online submissions for First Unique Character in a String.
        Memory Usage: 14.1 MB, less than 95.76% of Python3 online submissions for First Unique Character in a String.
        """
        htable = {}
        for i in s:
            if i in htable:
                htable[i]+=1
            else:
                htable[i]=1
        for key in htable:
            if htable[key] == 1:
                return s.index(key)
            if key == list(htable)[-1]:
                return -1
              
            
        