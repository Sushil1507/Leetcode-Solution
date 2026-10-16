class Solution(object):
    def mySqrt(self, x):
        if x < 0:
            return 0
        elif x < 2:
            return x

        left = 1
        right = x

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


# Testing code
sol = Solution()

print(sol.mySqrt(4))    # 2
print(sol.mySqrt(8))    # 2
print(sol.mySqrt(16))   # 4
print(sol.mySqrt(1))    # 1
print(sol.mySqrt(0))    # 0