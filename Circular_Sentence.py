class Solution(object):
    def isCircularSentence(self, s):
        if s[0] != s[-1]: return False
        flag = 1
        for ch in s:
            if flag:
                if ch != ' ': last = ch
                else: flag = 0
            else:
                if ch != last: return False
                flag = 1
        return True
