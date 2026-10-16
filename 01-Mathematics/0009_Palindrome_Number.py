class Solution(object):
    def isPalindrome(self, x):
        if x < 0 : 
            return False

        original = x
        reverse = 0

        while original > 0:
            rem = original % 10
            reverse = reverse * 10 + rem
            original //= 10

        if x == reverse:
            return True
        else:
            return False

sol = Solution()

print(sol.isPalindrome(121))   # True
print(sol.isPalindrome(-121))  # False
print(sol.isPalindrome(10))    # Fals