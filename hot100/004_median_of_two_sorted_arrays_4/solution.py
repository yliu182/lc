"""
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return
the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000

Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
"""

from typing import List


    # 1 3 5    4 8
    #     i

    # 3   5
    # j

# make sure nums1[0:i+1] and nums[0:j+1] contains half of the total elements


class Solution:
    def _get_medium(self, nums: List[int]):
        l = len(nums)
        if l % 2 == 0:
            return 0.5 * (nums[l//2] + nums[l//2 - 1])
        else:
            return nums[l//2]

    def _at(self, nums: List[int], idx :int):
        if idx < 0:
            return float('-inf')
        elif idx >= len(nums):
            return float('inf')
        else:
            return nums[idx]


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0:
            return self._get_medium(nums2)

        if len(nums2) == 0:
            return self._get_medium(nums1)

        # always put shorter list as first input
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        # for moving the i in a binary-search manner
        low = 0
        high = len(nums1)

        while low <= high:
            # i the number of elements, can choose between 0, 1, 2, ..., len(nums1)
            i = (low + high) // 2
            # i and j must contains half of the total element
            j = (len(nums1) + len(nums2) + 1) // 2 - i
            a_left = self._at(nums1, i - 1)
            a_right = self._at(nums1, i)
            b_left = self._at(nums2, j - 1)
            b_right = self._at(nums2, j)

            if a_left <= b_right and a_right >= b_left:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return max(a_left, b_left)
                else:
                    return 0.5 * (max(a_left, b_left) + min(a_right, b_right))

            if a_left > b_right:
                high = i - 1

            elif a_right < b_left:
                low = i + 1
                i = (low + high) // 2
