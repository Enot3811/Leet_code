"""Median of two sorted arrays.

Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10**6 <= nums1[i], nums2[i] <= 10**6
"""


from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) <= len(nums2):
        shortest = nums1
        longest = nums2
    else:
        shortest = nums2
        longest = nums1
    merged_len = len(shortest) + len(longest)
    median_el = merged_len // 2
    even = merged_len % 2 == 0

    r = len(shortest) - 1
    l = 0
    while (True):
        mid_shortest = (r + l) // 2
        mid_longest = median_el - mid_shortest

        left_shortest = shortest[mid_shortest] if mid_shortest >= 0 else float('-infinity')
        right_shortest = shortest[mid_shortest + 1] if mid_shortest + 1 < len(shortest) else float('infinity')
        left_longest = longest[mid_longest] if mid_longest >= 0 else float('-infinity')
        right_longest = longest[mid_longest + 1] if mid_longest + 1 < len(longest) else float('infinity')

        if left_shortest <= right_longest and left_longest <= right_shortest:
            if even:
                first = max(left_shortest, left_longest)
                second = min(right_shortest, right_longest)
                return (first + second) / 2
            else:
                return min(right_shortest, right_longest)
        elif left_shortest > right_longest:
            r = mid_shortest - 1
        else:
            l = mid_shortest + 1


if __name__ == '__main__':
    # [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
    arr2 = [1, 2, 3, 4, 5]
    print(findMedianSortedArrays(arr1, arr2))
