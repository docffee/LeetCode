class Solution:
    def minimumSum(self, num: int) -> int:
        # Runtime 32 ms 92.92%, Memory Usage 13.8 MB 96.00%
        # sort string then convert to num
        string = sorted(str(num))
        # 2-2 will always be less than 3-1
        #0999 -> 999+0, 099+9
        #0999 -> 09 + 99
        a = sorted((int(string[0])*10 + int(string[2]), int(string[1])*10 + int(string[3]), int(string[0])*10 + int(string[3]), int(string[1])*10 + int(string[2])))
        return a[0]+a[3]

    def minimumSum2(self, num: int) -> int:
        # Runtime 33.09%, Memory Usage 96.00%
        # sort string then convert to num
        string = sorted(str(num))
        # 2-2 will always be less than 3-1
        #0999 -> 999+0, 099+9
        #0999 -> 09 + 99
        a = int(string[0])*10 + max(int(string[2]), int(string[3]))
        b = int(string[1])*10 + min(int(string[3]),int(string[2]))
        return a+b