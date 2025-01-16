"""
https://leetcode.com/problems/reverse-integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
    Input: x = 123
    Output: 321

Example 2:
    Input: x = -123
    Output: -321

Example 3:
    Input: x = 120
    Output: 21

Constraints:
    -2^31 <= x <= 2^31 - 1
"""


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
