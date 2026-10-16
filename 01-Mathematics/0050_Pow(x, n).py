class Solution(object):
    def myPow(self, x, n):
        return pow(x, n)


# Testing code
sol = Solution()

print(sol.myPow(2.0, 10))    # 1024.0
print(sol.myPow(2.1, 3))     # 9.261
print(sol.myPow(2.0, -2))    # 0.25