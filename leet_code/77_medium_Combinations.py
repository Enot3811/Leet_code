"""Combinations.

Given two integers n and k, return all possible combinations of k numbers
chosen from the range [1, n].

You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e.,
[1,2] and [2,1] are considered to be the same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

Constraints:
1 <= n <= 20
1 <= k <= n
"""


# from itertools import combinations
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def combine_next(n: int, k: int, start: int):
            global answer, combined_numbers
            for i in range(start, n):
                combined_numbers.append(i)
                if len(combined_numbers) < k:
                    combine_next(n, k, combined_numbers[-1] + 1)
                else:
                    answer.append(combined_numbers[:])
                combined_numbers.pop()

        n += 1
        global answer, combined_numbers
        answer = []
        combined_numbers = []
        combine_next(n, k, 1)
        return answer


if __name__ == '__main__':
    sol = Solution()
    print(sol.combine(6, 3))
# print(list(combinations([*range(1, 6+1)], 3)))
