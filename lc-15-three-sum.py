"""
https://leetcode.com/problems/3sum/description/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation:
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.

Constraints:
    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 1st easy case: (0,0,0)
        # 2nd easy case: (-i,0,i)
        # hard case: (-i,j,k) or (-i,-j,k)
        out: set[tuple[int, int, int]] = set()

        neg: list[int] = []
        pos: list[int] = []
        numZeroes: int = 0
        for n in nums:
            if n > 0:
                pos.append(n)
            elif n < 0:
                neg.append(n)
            else:
                numZeroes += 1

        if numZeroes > 2:
            out.add((0, 0, 0))
        if numZeroes > 0:
            for n in neg:
                if -n in pos:
                    out.add((-n, 0, n))

        # 4. For all pairs of negative numbers
        # check to see if their complement
        # exists in the positive number set
        from itertools import combinations

        for x, y in combinations(neg, 2):
            target = -1 * (x + y)
            if target in pos:
                out.add(tuple(sorted([x, y, target])))

        # 5. For all pairs of positive numbers
        # check to see if their complement
        # exists in the negative number set

        for x, y in combinations(pos, 2):
            target = -1 * (x + y)
            if target in neg:
                out.add(tuple(sorted([x, y, target])))

        return list(out)

    def threeSumNaive(self, nums: list[int]) -> list[list[int]]:
        out: set[int] = set()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        out.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return list(out)
