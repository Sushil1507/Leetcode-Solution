class Solution(object):
    def reverse(self, x):

        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0

        while x > 0:
            rem = x % 10
            rev = rev * 10 + rem
            x //= 10

        rev = rev * sign

        if rev < INT_MIN or rev > INT_MAX:
            return 0

        return rev


# Testing code
sol = Solution()

print(sol.reverse(123))          # 321
print(sol.reverse(-123))         # -321
print(sol.reverse(120))          # 21
print(sol.reverse(1534236469))   # 0