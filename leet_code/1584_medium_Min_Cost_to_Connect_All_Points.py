"""1584. Min Cost to Connect All Points

Check the images!
https://leetcode.com/problems/min-cost-to-connect-all-points/

You are given an array points representing integer coordinates of some points
on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance
between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected.
All points are connected if there is exactly one simple path between any two points.

Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

Constraints:
1 <= points.length <= 1000
-10**6 <= xi, yi <= 10**6
All pairs (xi, yi) are distinct.
"""

# Размышления
# Задача может быть решена несколькими способами.
# 1) Более интуитивный и, как оказалось, более эффективный
# Берём случайную точку, считаем его дистанции до остальных точек.
# Отбираем минимальное ребро и соединяем.
# Теперь, когда они вместе, дистанции второй точки являются дистанциями и для первой,
# так что обновляем список дистанций, получаем новые минимумы.
# И так пока не соединим все точки.
# В итоге n итераций, и на каждой нужно считать n связей с поиском минимума - n**2
# По памяти скромнее - список дистанций для одной точки - n


from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def calculate_dist(x1: int, y1: int, x2: int, y2: int) -> int:
            return abs(x1 - x2) + abs(y1 - y2)

        # Изначальные дистанции, чтобы добавить обработку нулевой точки в общем виде
        dists = {i: float('inf') for i in range(len(points))}
        dists[0] = 0

        ans = 0
        while len(dists) > 0:
            # Берём точку, к которой ведёт минимальное ребро.
            # Считаем, что мы присоединили её
            next_p = min(dists, key=dists.get)
            # Убираем эту точку, чтобы не считать расстояния до неё
            ans += dists.pop(next_p)
            # Пересчитываем дистанции с расчётом на новую точку
            for p_idx, dist in dists.items():
                new_dist = calculate_dist(*points[next_p], *points[p_idx])
                dists[p_idx] = min(dist, new_dist)
        return ans


# 2) Union find
# Считаем все-все-все рёбра, сохраняем их как (dist, p1_i, p2_i) и сортируем по dist.
# Получаем список ранжированный по длине рёбер.
# Проходим по нему и делаем union find между двумя точками.
# Если две точки принадлежат к разным деревьям, то у них будет разный родитель,
# и мы присоединим одно дерево к другому, обновив родителей.
# Если одинаковые, то мы это увидим и просто перейдём дальше.
# Делаем до тех пор, пока не наберём n-1 рёбер (минимально связанный граф).
# По скорости будет n**2 (при вычислении рёбер, а затем ещё и проход по ним).
# По памяти тоже n**2 (все рёбра)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def calculate_dist(x1: int, y1: int, x2: int, y2: int) -> int:
            return abs(x1 - x2) + abs(y1 - y2)
        # Посчитаем все возможные рёбра и отсортируем их по длине
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges.append((calculate_dist(*points[i], *points[j]), i, j))
        edges.sort(key=lambda x: x[0])

        # Union find
        parents = list(range(len(points)))
        rank = [1,] * len(points)
        def find(point_n: int) -> int:
            if point_n != parents[point_n]:
                parents[point_n] = find(parents[point_n])
            return parents[point_n]
        def union(point_i: int, point_j: int) -> bool:
            parent_i = find(point_i)
            parent_j = find(point_j)
            if parent_i != parent_j:
                if rank[parent_i] > rank[parent_j]:
                    parents[parent_j] = parent_i
                elif rank[parent_i] < rank[parent_j]:
                    parents[parent_i] = parent_j
                else:
                    parents[parent_j] = parent_i
                    rank[parent_i] += 1
                return True
            return False

        # Проходим по всем рёбрам и пробуем соединять деревья (изначально точки)
        # между собой.
        # Если точки уже в одной компоненте связности,
        # то union find покажет один и тот же корень.
        # Если нет, то связываем.
        # В итоге рёбер должно быть n-1, а union find гарантирует отсутствие циклов.
        edge_count = 0
        overall_dist = 0
        for w, point_i, point_j in edges:
            if union(point_i, point_j):
                edge_count += 1
                overall_dist += w
                if edge_count == len(points) - 1:
                    break
        return overall_dist
    

sol = Solution()
sol.minCostConnectPoints([[7,18],[-15,19],[-18,-15],[-7,14],[4,1],[-6,3]])
