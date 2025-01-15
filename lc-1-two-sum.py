"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
"""

import unittest


class Solution:
    def naiveTwoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Space: O(1)
        Time: O(N^2)
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]

    def sortTwoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Space: O(N)
        Time: O(N log N) + O(N)
        """
        numsWithIdx: list[tuple[int, int]] = list(zip(nums, range(len(nums))))
        sortedNums: list[tuple[int, int]] = sorted(
            numsWithIdx, key=lambda pair: pair[0]
        )
        i = 0
        j = len(sortedNums) - 1
        while True:
            i_idx = sortedNums[i][1]
            j_idx = sortedNums[j][1]
            if sortedNums[j][0] > target:
                j -= 1
            if sortedNums[i][0] + sortedNums[j][0] == target:
                return [i_idx, j_idx]
            if sortedNums[i][0] + sortedNums[j][0] > target:
                j -= 1
            if sortedNums[i][0] + sortedNums[j][0] < target:
                i += 1
        return [-1, -1]

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Space: O(N)
        Time: O(N)
        """

        pairingToIdx: dict[int, int] = {}
        for i in range(len(nums)):
            if nums[i] in pairingToIdx:
                return [i, pairingToIdx[nums[i]]]
            pairingToIdx[target - nums[i]] = i
        return [-1, -1]


class TestTwoSumNaive(unittest.TestCase):
    def test_sort_two_sum(self):
        test1 = [2, 7, 11, 15]
        test2 = [3, 2, 4]
        test3 = [3, 3]

        sol = Solution()
        self.assertEqual(
            sol.naiveTwoSum(nums=test1, target=9), [0, 1], "Should be [0, 1]"
        )
        self.assertEqual(
            sol.naiveTwoSum(nums=test2, target=6), [1, 2], "Should be [1, 2]"
        )
        self.assertEqual(
            sol.naiveTwoSum(nums=test3, target=6), [0, 1], "Should be [0, 1]"
        )


class TestTwoSumSorted(unittest.TestCase):
    def test_sort_two_sum(self):
        test1 = [2, 7, 11, 15]
        test2 = [3, 2, 4]
        test3 = [3, 3]

        sol = Solution()
        self.assertEqual(
            sol.sortTwoSum(nums=test1, target=9), [0, 1], "Should be [0, 1]"
        )
        self.assertEqual(
            sol.sortTwoSum(nums=test2, target=6), [1, 2], "Should be [1, 2]"
        )
        self.assertEqual(
            sol.sortTwoSum(nums=test3, target=6), [0, 1], "Should be [0, 1]"
        )


class TestTwoSum(unittest.TestCase):
    def test_sort_two_sum(self):
        test1 = [2, 7, 11, 15]
        test2 = [3, 2, 4]
        test3 = [3, 3]

        sol = Solution()
        self.assertEqual(
            sorted(sol.sortTwoSum(nums=test1, target=9)), [0, 1], "Should be [0, 1]"
        )
        self.assertEqual(
            sorted(sol.sortTwoSum(nums=test2, target=6)), [1, 2], "Should be [1, 2]"
        )
        self.assertEqual(
            sorted(sol.sortTwoSum(nums=test3, target=6)), [0, 1], "Should be [0, 1]"
        )


if __name__ == "__main__":
    unittest.main()
