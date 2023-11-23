"""Gas Station."""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diffs = [g - c for g, c in zip(gas, cost)]
        if sum(diffs) < 0:
            return -1
        accum = 0
        start_idx = None
        for i, diff in enumerate(diffs):
            if start_idx is None:
                if diff >= 0:
                    start_idx = i
                    accum = diff
            else:
                accum += diff
            if accum < 0:
                start_idx = None
        return start_idx


sol = Solution()
tests = [
    ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
    ([2, 3, 4], [3, 4, 3], -1),
    ([3, 7, 11, 3, 1, 5], [10, 6, 5, 1, 3, 5], 1),
    ([11], [1], 0),
    ([1], [11], -1),
    ([1], [1], 0),
    ([0, 0, 0, 4], [1, 1, 1, 1], 3),
    ([14, 5, 2, 7, 9, 0, 1, 4, 6, 2, 22, 0, 1], [3, 10, 5, 1, 6, 8, 2, 4, 7, 10, 11, 4, 2], 10)
]
for gas, cost, ans in tests:
    out = sol.canCompleteCircuit(gas, cost)
    print('ans:', out, 'exp:', ans)
