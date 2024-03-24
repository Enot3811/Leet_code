"""Subsets.

Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets.
Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for number in nums:
            answer.append([number])
            if len(answer) >= 2:
                last = len(answer) - 1
                for i in range(last):
                    answer.append(answer[i] + answer[last])
        answer.append([])
        return answer


if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets([1, 2, 3, 4]))
