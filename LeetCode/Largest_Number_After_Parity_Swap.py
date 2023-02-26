class Solution:
    def largestInteger(self, num: int) -> int:
        """Runtime 34 ms Beats 73.52% Memory 13.8 MB Beats 98.35%"""
        digits = [int(d) for d in str(num)]
        odd = sorted([d for d in digits if d%2 != 0])
        even = sorted([d for d in digits if d%2 == 0])
        resDigits =[even.pop() if digits[i]%2==0 else odd.pop() for i in range(len(digits))]
        return int(''.join([str(d) for d in resDigits]))