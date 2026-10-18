class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"

        result = []

        if (numerator < 0) != (denominator < 0):
            result.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        result.append(str(numerator // denominator))
        remainder = numerator % denominator

        if remainder == 0:
            return "".join(result)

        result.append(".")
        seen = {}

        while remainder != 0:
            if remainder in seen:
                result.insert(seen[remainder], "(")
                result.append(")")
                break

            seen[remainder] = len(result)

            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(result)

sol = Solution()

print(sol.fractionToDecimal(1,2)) # 0.5
print(sol.fractionToDecimal(2,1)) #2
print(sol.fractionToDecimal(4,333)) # 0.(012)