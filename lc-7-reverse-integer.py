class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0 and x < 10:
            return x
        string = str(abs(x))
        reversedString = string[::-1]
        result = int(reversedString.lstrip("0"))
        if x < 0:
            result *= -1
        if result <= -(2**31) or result >= 2**31 - 1:
            return 0
        return result
