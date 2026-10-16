
class Solution(object):
    def isHappy(self, n):
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            total = 0

            while n > 0:
                rem = n % 10
                total = total + rem * rem
                n //= 10

            n = total

        return True


sol = Solution()
print(sol.isHappy(19))  # True
print(sol.isHappy(2))   # False
print(sol.isHappy(7))   # True
