"""455. Assign Cookies."""

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child_count = 0
        for cookie in s:
            if cookie >= g[child_count]:
                child_count += 1
                if child_count == len(g):
                    break
        return child_count


sol = Solution()
examples_g = [
    [1, 2, 3],
    [1, 2],
    [7, 1, 4],
    [1],
    [1, 2],
    [3, 3, 3, 3],
    [3, 3, 3, 1]
]
examples_s = [
    [1, 1],
    [1, 2, 3],
    [6, 3, 6],
    [],
    [],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]
for g, s in zip(examples_g, examples_s):
    print(sol.findContentChildren(g, s))
