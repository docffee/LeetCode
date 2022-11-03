class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Runtime: 69 ms, faster than 44.76% of Python3 online submissions for Longest Common Prefix.
        Memory Usage: 13.8 MB, less than 88.32% of Python3 online submissions for Longest Common Prefix.

        """
        out = []
        #find smallest word in list and set as range
        for i in range(min(map(len,strs))):
            #iterate each letter in each word if common will equal 1
            if len(set([s[i] for s in strs])) == 1:
                #add letter to list
                out.append(strs[0][i])
            else:
                break
        #return list as string
        return ''.join(out)