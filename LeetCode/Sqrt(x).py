class Solution(object):
    def mySqrt_binary_search(self, x):
        """
        :typex: int
        :rtype: int
        """
        left = 0
        right = x
        while 1 + left < right:
            mid = (l+r)/2
            if mid*mid>x: r=mid
            if mid*mid<x: l=mid
            if mid*mid==x: return int(mid)
        if right*right == x: return int(right)
        
        return int((1+r)/2)

    def mySqrt(self, x):
        left = 1
        right = x // 2
        while left<right:
            mid = left + (right - left) // 2
            if mid > x/mid:
                right = mid - 1
            else:
                left = mid - 1
        return left - 1