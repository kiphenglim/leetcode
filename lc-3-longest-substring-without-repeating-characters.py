"""
https://leetcode.com/problems/longest-substring-without-repeating-characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
    0 <= s.length <= 5 * 10^4
    s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        startIdx: int = 0
        maxsubstr: int = 0
        charToIdx: dict[str, int] = {}

        for endIdx in range(len(string)):
            char = string[endIdx]
            if char in charToIdx and charToIdx[char] >= startIdx:
                startIdx = charToIdx[char] + 1
            charToIdx[char] = endIdx
            maxsubstr = max(maxsubstr, endIdx - startIdx + 1)

        return maxsubstr
