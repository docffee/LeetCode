class Solution(object):
    def isStrobogrammatic(num):
        """
        :type num: str
        :rtype: bool
        """
        rotated_digits = ['0', '1', '', '', '', '', '9', '', '8', '6']
        
        rotated_string = []
        
        for i in reversed(num):
            rotated_string.append(rotated_digits[int(i)])
        
        testcase = "".join(rotated_string)
        return testcase == num

num = str(69676969)
print(Solution.isStrobogrammatic(num))