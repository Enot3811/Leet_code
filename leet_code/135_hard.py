"""Candy."""

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        result_map = [1] * len(ratings)

        # Слева направо
        # Составляется карта подъёмов
        for i in range(1, len(ratings)):
            # Если следующий больше, то даём ему +1
            if ratings[i] > ratings[i - 1]:
                result_map[i] = result_map[i - 1] + 1
        
        # Справа налево
        # Составляется карта спусков
        for i in range(len(ratings) - 2, -1, -1):
            # Если следующий больше, то даём ему +1
            if ratings[i] > ratings[i + 1] and result_map[i] <= result_map[i + 1]:
                result_map[i] = result_map[i + 1] + 1
        return sum(result_map)


sol = Solution()
tests = [
    ([1,0,2], 5),
    ([1,2,2], 4),
    ([1, 2, 3, 4, 3, 2, 1], 16),
    ([5, 1, 3, 9, 9, 5, 5, 1, 2, 4], 19),
    ([2, 3, 5, 1, 3, 9, 9, 5, 5, 1, 2, 4], 23),
    ([2, 3, 5, 1, 3, 9, 9, 7, 6, 5, 5, 5, 1, 2, 4], 31),
]
for inp, ans in tests:
    out = sol.candy(inp)
    print('ans:', out, 'exp:', ans)
