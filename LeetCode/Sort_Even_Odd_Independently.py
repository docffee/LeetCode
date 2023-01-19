class Solution:
    def sortEvenOdd(self, A):
        """Runtime 47 ms Beats 97.42% Memory 13.9 MB Beats 63.82%"""
        A[::2], A[1::2] = sorted(A[::2]), sorted(A[1::2])[::-1]
        return A