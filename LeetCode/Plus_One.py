def plusOneRecursion(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    if len(digits) == 0:
        digits = [1]
    elif digits[-1] == 9:
        digits = self.plusOne(digits[:-1])
        digits.extend([0])
    else:
        digits[-1] += 1
    return digits

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[0] !=9 and digits[-1] == 9:
            new_digits = [digits[0]+1]
            for index in range(len(digits),0,-1):
                new_digits.extend([0])
        elif len(digits) == 1 and digits[0] == 9:
            return [1,0]
            return new_digits
        elif digits[0] == 9 and digits[-1] == 9:
            new_digits = [1]
            for index in range(len(digits),0,1):
                new_digits.extend([0])
        else:
            digits[-1] = digits[-1]+1
            return digits