"""Apple Redistribution into Boxes."""

from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        capacity.sort(reverse=True)
        for i, box in enumerate(capacity):
            apples -= box
            if apples <= 0:
                return i + 1
            

if __name__ == '__main__':
    cases = [
        ([5, 4, 1], [1, 2, 10], 1),
        ([1, 3, 2], [4, 3, 1, 5, 2], 2),
        ([5, 5, 5], [2, 4, 2, 7], 4)
    ]
    sol = Solution()
    for apple, capacity, ans in cases:
        res = sol.minimumBoxes(apple, capacity)
        print('Got:', res, 'Exp:', ans)
