from timeit import timeit


class Solution(object):
    def isStrobogrammatic(num):
        """
        :type num: str
        :rtype: bool
        """
        # Rotate 180 degrees = reverse image + flip image upside down
        rotated_digits = ['0', '1', '', '', '', '', '9', '', '8', '6']
        
        rotated_string = []
        
        for char in reversed(num): # reverse image
            rotated_string.append(rotated_digits[int(char)])  # flip image upside down
        
        testcase = "".join(rotated_string)
        return testcase == num

num = str(69676969)
print(Solution.isStrobogrammatic(num))