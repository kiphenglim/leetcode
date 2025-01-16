"""
https://leetcode.com/problems/palindrome-number/description/

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
    -2^31 <= x <= 2^31 - 1

Follow up: Could you solve it without converting the integer to a string?
"""

from collections import deque


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        dq = deque()
        while x != 0:
            digit = x % 10
            dq.appendleft(digit)
            x = x // 10
        while len(dq) > 1:
            if dq.pop() != dq.popleft():
                return False
        return True
