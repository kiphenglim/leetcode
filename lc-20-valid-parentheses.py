"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
  * Open brackets must be closed by the same type of brackets.
  * Open brackets must be closed in the correct order.
  * Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "()"
    Output: true
Example 2:
    Input: s = "()[]{}"
    Output: true
Example 3:
    Input: s = "(]"
    Output: false
Example 4:
    Input: s = "([])"
    Output: true

Constraints:
    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        valid = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        open_ch = {"(", "[", "{"}

        for ch in s:
            if ch in open_ch:
                stack.append(ch)
                continue
            if ch not in valid:
                return False
            if len(stack) == 0 or stack[len(stack) - 1] != valid[ch]:
                return False
            stack.pop()
        return stack == []
