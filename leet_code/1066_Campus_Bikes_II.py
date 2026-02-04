"""1066. Campus Bikes II

Premium lock.
https://leetcode.doocs.org/en/lc/1066/

On a campus represented as a 2D grid, there are n workers and m bikes, with n <= m.
Each worker and bike is a 2D coordinate on this grid.

We assign one unique bike to each worker so that the sum of the Manhattan distances
between each worker and their assigned bike is minimized.

Return the minimum possible sum of Manhattan distances between each worker
and their assigned bike.

The Manhattan distance between two points p1 and p2 is
Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Example 1:
Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: 6
Explanation: 
We assign bike 0 to worker 0, bike 1 to worker 1. The Manhattan distance of both assignments is 3, so the output is 6.

Example 2:
Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
Output: 4
Explanation: 
We first assign bike 0 to worker 0, then assign bike 1 to worker 1 or worker 2,
bike 2 to worker 2 or worker 1.
Both assignments lead to sum of the Manhattan distances as 4.

Example 3:
Input: workers = [[0,0],[1,0],[2,0],[3,0],[4,0]],
bikes = [[0,999],[1,999],[2,999],[3,999],[4,999]]
Output: 4995

Constraints:
n == workers.length
m == bikes.length
1 <= n <= m <= 10
workers[i].length == 2
bikes[i].length == 2
0 <= workers[i][0], workers[i][1], bikes[i][0], bikes[i][1] < 1000
All the workers and the bikes locations are unique.
"""

# Теги
# Поиск в глубину (dfs)

# Размышления
# Сначала можем показаться, что задача идеально ложится на DP,
# что решаем задачу с разным количеством людей.
# Но на самом деле там возникают проблемы, что текущий элемент не знает,
# какие велики уже заняты, и по итогу несколько человек берут 1 ближайший к ним обоим.
# Проще решить через dfs, где мы явно указываем из каких великов выбирать.
# Проблема здесь лишь в том, что сложность получается экспоненциальная.
# К i-му человеку может прийти огромное число перестановок из оставшихся великов.
# Если представить bikes как битовую маску, указывающую занят ли велик,
# то у неё 2^k состояний.
# И при том для каждого человека, то есть n*2^k.
# Битовая маска также позволит оптимизировать мемоизацию и аргументы.
# Вместо явной передачи списка оставшихся великов лучше использовать битовую маску.

from typing import List

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        memory = {}

        def dfs(worker_idx: int, bikes_mask: int) -> int:
            if worker_idx >= len(workers):
                return 0
            save_idx = (worker_idx, bikes_mask)
            if save_idx in memory:
                return memory[save_idx]
            worker_x, worker_y = workers[worker_idx]
            optim = float("inf")
            for i, bike in enumerate(bikes):
                # Проверяем, свободен ли велосипед i (бит i равен 0)
                if not (bikes_mask & (1 << i)):
                    bike_x, bike_y = bike
                    dist = abs(worker_x - bike_x) + abs(worker_y - bike_y)
                    optim = min(
                        optim,
                        # Установим нужный бит в 1
                        dist + dfs(worker_idx + 1, bikes_mask | (1 << i)))
            memory[save_idx] = optim
            return optim

        return dfs(0, 0)

cases = [
    (([[0,0],[1,1],[2,2]], [[2,3],[1,10],[0,-1],[1,-2]]), 5),
    (([[0,0],[1,1]], [[1,0],[10,1]]), 10),
    (([[0,0],[2,1]], [[1,2],[3,3]]), 6),
    (([[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]]), 4),
    (([[0,0],[1,0],[2,0],[3,0],[4,0]], [[0,999],[1,999],[2,999],[3,999],[4,999]]), 4995),
]
sol = Solution()
for inp, ans in cases:
    res = sol.assignBikes(*inp)
    print(inp, res, ans)
