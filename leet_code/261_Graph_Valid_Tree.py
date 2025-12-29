"""261. Graph Valid Tree

Premium lock on leetcode.
https://www.lintcode.com/problem/178/

Given n nodes labeled from 0 to n - 1 and a list of undirected edges
(each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.

Example 1:
Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true

Example 2:
Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false
"""

# Размышления
# С первого взгляда задача кажется совсем простой, но есть подводный камень.
# Рёбра не обязаны исходить из корня, так как они ненаправленные.
# То есть появляются кейсы вроде [[1,0],[2,0]].
# То есть не получится просто set visited и не допускать появление вершины более 1 раза.
# Потому придётся делать более основательно.
# Нам требуется, чтобы граф был без циклов и полносвязный.
# Можно заметить, что чтобы в графе не было циклов, в нём должно быть не более n-1 рёбер
# То есть везде по 1 ребру, чтобы соединить 2 ноды и получить полносвязный граф.
# А полносвязный граф у нас будет если рёбер не менее n-1.
# То есть по итогу уже одно жёсткое условие: рёбер == n-1.
# Но это условие всё ещё не гарантирует ни первого, ни второго.
# Например: n=5 [[0,1],[2,3],[3,4],[4,2]]. Рёбер n-1, но при этом граф разделён на две
# части, и во второй есть цикл.
# То есть по-мимо этого условия нужно проверить ещё одно из двух верхних.
# Мы можем легко проверить полносвязность собрав карту смежности из рёбер
# и пройдя по ней с целью посетить все ноды.
# И тогда для циклов просто не останется свободных рёбер.

from collections import defaultdict, deque
from typing import List

class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        # Собираем смежности
        adj = defaultdict(list)
        for st, end in edges:
            # Нужна возможность пройти в обе стороны
            # Например [[1,0], [2,0]]. Из 1 придём в 0, но не сможем прийти в 2.
            adj[st].append(end)
            adj[end].append(st)

        # Не принципиально с какой начинать, всё равно мы должны в итоге прийти во все
        visited = set()
        visited.add(0)
        queue = deque([0])
        while len(queue) > 0:
            curr_node = queue.pop()
            for neighbor in adj[curr_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        # Если мы из какой-то ноды смогли посетить все, то он полносвязный
        return len(visited) == n


cases = [
    ((3, [[1,0],[2,0]]), True),
    ((5, [[4,0],[2,0],[1,3],[3,4]]), True),
    ((5, [[4,0],[2,0],[1,3]]), False),
    ((5, [[0, 1], [0, 2], [0, 3], [1, 4]]), True),
    ((5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False),
    ((5, [[0, 1], [2, 3], [2, 4]]), False),
    ((1, []), True),
    ((5, [[0,1],[1,2],[2,3],[3,4],[4,0]]), False),
    ((5, [[0,1],[1,2],[3,4],[4,0]]), True),
    ((5, [[0,1],[1,2],[2,3],[3,4]]), True),
]
sol = Solution()
for inp, ans in cases:
    res = sol.valid_tree(*inp)
    print(inp, res, ans)
