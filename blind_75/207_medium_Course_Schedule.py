"""207. Course Schedule

https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take,
labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0
you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also
have finished course 1. So it is impossible.

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

# Размышления
# Задача на графы, где необходимо определить, есть ли в графе циклы.
# По сути prerequisites составляют подобие направленного графа.
# Для начала необходимо составить список смежностей,
# чтобы с этим графом можно было работать. Это приводит к памяти n^2, но так надо.
# Затем мы можем пройтись по всем вершинам по порядку, делая dfs по списку смежностей.
# Чтобы понять, что мы сделали цикл, введём ещё один буфер памяти visited на n.
# Цель очистить список смежностей, проверив все цепочки.

from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Какие курсы требует каждый курс, или список смежности
        prerequisites_map = defaultdict(list)
        for want, need in prerequisites:
            prerequisites_map[want].append(need)
        
        visited = set()
        def dfs(course: int):
            if course in visited:
                return False
            if course not in prerequisites_map:
                return True

            visited.add(course)
            for need in prerequisites_map[course]:
                if not dfs(need):
                    return False
            prerequisites_map.pop(course)
            visited.remove(course)
            return True

        for want in range(numCourses):
            if not dfs(want):
                return False
        return True

# Алгоритм Кана
# Сортирует направленный граф так, что сначала идут ноды без требований, а потом те,
# на которые направлены другие ноды.
# В общем, идеально подходит под подобные задачи, где у задач есть предварительные
# требования к другим задачам.
# Алгоритм не дорабатывает до конца, если в графе есть циклы, что нам и поможет.
# Идея в том, что мы заполняем счётчики требований каждой ноде.
# Потом берём ноды, у которых счётчики нулевые (нет требований).
# Проходим по списку смежностей, смотрим, кому они требуются.
# -1 для всех, кто их требует.
class Solution:
    def canFinish(self, numCourses, prerequisites):
        requires_curses = [0] * numCourses  # Сколько курсов требует каждый курс
        adj = [[] for _ in range(numCourses)]  # Список смежностей

        # Заполняем список так, чтобы потом было удобно смотреть, кому этот курс нужен
        # И +1 в нужный счётчик
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            requires_curses[prerequisite[0]] += 1

        queue = deque()
        for i in range(numCourses):
            if requires_curses[i] == 0:
                queue.append(i)

        # Все ноды должны пройти через очередь
        nodesVisited = 0
        while queue:
            node = queue.popleft()
            nodesVisited += 1

            # Перебираем, кому нужна эта нода
            for neighbor in adj[node]:
                requires_curses[neighbor] -= 1
                if requires_curses[neighbor] == 0:
                    queue.append(neighbor)

        # Если не все прошли, значит у кого-то до сих пор остались требования
        # а это указывает на наличие циклов
        return nodesVisited == numCourses


sol = Solution()
cases = [
    ((10, [[3,4],[6,7],[6,8]]), True),
    ((10, [[3,4],[8,3],[4,8]]), False),
    ((10, []), True),
    ((4, [[1,2],[2,3],[3,4],[4,1]]), False),
    ((4, [[1,2],[2,3],[3,4],[1,4]]), True),
    ((10, [[3,4],[4,5],[5,6],[1,4],[4,7],[7,8]]), True),
    ((10, [[3,4],[4,5],[5,7],[1,4],[4,7],[7,8]]), True),
    ((10, [[3,4],[4,5],[5,8],[1,4],[4,7],[7,8]]), True),
    ((10, [[3,4],[4,5],[5,1],[1,4],[4,7],[7,8]]), False),
]
for inp, ans in cases:
    res = sol.canFinish(*inp)
    print(inp, res, ans)