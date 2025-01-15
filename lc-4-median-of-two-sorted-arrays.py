from math import ceil, floor
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combinedList = nums1
        combinedList.extend(nums2)
        combinedList.sort()
        midIdx = (len(combinedList) - 1) / 2
        if type(midIdx) is int:
            return combinedList[ceil(midIdx)]
        low = floor(midIdx)
        high = ceil(midIdx)
        return (combinedList[low] + combinedList[high]) / 2
