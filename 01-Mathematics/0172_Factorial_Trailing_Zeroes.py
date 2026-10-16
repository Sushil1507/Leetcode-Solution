
class Solution(object):
    def trailingZeroes(self, n):
        count = 0

        while n >= 5:
            n //= 5
            count += n

        return count


sol = Solution()
print(sol.trailingZeroes(5))    # 1
print(sol.trailingZeroes(10))   # 2
print(sol.trailingZeroes(25))   # 6
print(sol.trailingZeroes(100))  # 24
