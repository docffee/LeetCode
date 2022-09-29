class Solution:
    def is_palindrome(x) -> bool:
        if x < 0:
            return False

        # Find log10 of number
        div=1
        while x >= 10 * div:
            div*= 10

        while x:
            right = x % 10      # Find first digit to compare
            left = x // div     # Find second digit with floor division

            if left != right:   
                return False
                
            x = (x % div) // 10  # Divide by log10 to elim second then 10 to elim first
            div = div/100        # Divide by 100 to reduce counter to match size reduction
        return True

x = 1221
y = -56
z = 321
print(x)
print(Solution.is_palindrome(x))
print(y)
print(Solution.is_palindrome(y))
print(z)
print(Solution.is_palindrome(z))