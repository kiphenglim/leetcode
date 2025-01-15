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
