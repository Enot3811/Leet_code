"""Subarray Sum Equals K

Given an array of integers nums and an integer k,
return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
"""


from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Previous cumulative sum alg
        prev_sums = {}
        cur_sum = 0
        answer = 0
        for num in nums:

            cur_sum += num
            if cur_sum == k:
                answer += 1

            diff = cur_sum - k
            if diff in prev_sums:
                answer += prev_sums[diff]

            if cur_sum in prev_sums:
                prev_sums[cur_sum] += 1
            else:
                prev_sums[cur_sum] = 1

        return answer


sol = Solution()
examples = [
    (([1, 2, -2, -1], 0), 2),
    (([4, 5, 1, 2],3),1),
    (([1,1,1],2),2),
    (([1,2,3],3),2),
    (([1],1),1),
    (([1],2),0),
    (([0, 0, 0, 0, 0], 0), 15),
    (([1, 2, 3, -1, 4, -4, 1], 3), 4)
]

for inp, ans in examples:
    out = sol.subarraySum(*inp)
    print(inp, out, ans)
