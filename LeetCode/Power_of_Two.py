class Solution:    
    def isPowerOfTwo(self, n):
        """
        Runtime: 77 ms, faster than 9.18% of Python3 online submissions for Power of Two.
        Memory Usage: 13.9 MB, less than 9.93% of Python3 online submissions for Power of Two.
        """
        pow_of_2 = set(2**i for i in range(31))
        return n in pow_of_2