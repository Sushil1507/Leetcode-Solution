
class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False

        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor

        if n == 1:
            return True
        return False


sol = Solution()
print(sol.isUgly(6))    # True
print(sol.isUgly(1))    # True
print(sol.isUgly(14))   # False
print(sol.isUgly(0))    # False
print(sol.isUgly(-6))   # False
