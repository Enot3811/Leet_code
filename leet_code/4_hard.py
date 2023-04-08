'''Median of two sorted arrays.'''


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
        mid_longest = median_el - (mid_shortest + 1) - 1

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
