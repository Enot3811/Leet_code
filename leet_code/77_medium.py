'''Combinations.'''


# from itertools import combinations
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def combine_next(n: int, k: int, start: int):
            global answer, combined_numbers
            for i in range(start, n - (k - len(combined_numbers)) + 1):
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


sol = Solution()
print(sol.combine(6, 3))


# print(list(combinations([*range(1, 6+1)], 3)))
