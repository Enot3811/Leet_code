"""210. Course Schedule II

https://leetcode.com/problems/course-schedule-ii/

There are a total of numCourses courses you have to take,
labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0
you have to first take course 1.
Return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them.
If it is impossible to finish all courses, return an empty array. 

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So the correct course order is [0,1]

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take.
To take course 3 you should have finished both courses 1 and 2.
Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""

# Размышления
# Продолжение задачи Course Schedule (207).
# Уже в той задаче можно было использовать топологическую сортировку (topological sort),
# а в этой это обязательно.
# Алгоритм ранжирует ноды направленного графа от "старта" до конечных веток.
# То есть сначала ноды, из которых выходят стрелки, а потом ноды, в которые эти стрелки
# приходят.
# Суть проста:
# Проходим по данным рёбрам.
# Собираем список счётчиков зависимостей, сколько других нод требует i-я нода.
# И словарь вида "номер ноды: список, кто в ней нуждается".
# Потом отбираем ноды, у которых нет зависимостей, начинаем проход с них.
# При проходе пользуемся ранее собранными данными: список тех, кто в ней нуждается и
# уменьшаем им счётчики.
# Если счётчик упал до нуля, то эта нода уже получила все нужные связи, можно добавить.
# В итоге если в графе не было циклов, то мы пройдём по всем нодам.

from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Словарь вида "курс: список, кто в нём нуждается"
        prereqs = {i: [] for i in range(numCourses)}
        # Счётчики зависимостей, сколько курсов требует i-й курс
        n_prereqs = [0,] * numCourses
        # Заполняем эти данные
        for u, v in prerequisites:
            n_prereqs[u] += 1
            prereqs[v].append(u)

        # Закинем в очередь тех, у кого нет требований
        queue = deque()
        for course, n_prereq in enumerate(n_prereqs):
            if n_prereq == 0:
                queue.append(course)

        # Извлекаем курс, у которых нет требований
        # Проходим по курсам, которые нуждались в этом курсе
        # Уменьшаем их требования
        ans = []
        while len(queue) > 0:
            curr_course = queue.popleft()
            ans.append(curr_course)
            for course in prereqs[curr_course]:
                n_prereqs[course] -= 1
                if n_prereqs[course] == 0:
                    queue.append(course)
        
        # В конце должны быть все курсы. Иначе невозможно решить
        return ans if len(ans) == numCourses else []

cases = [
    ((2, [[1,0]]),[0,1]),
    ((4, [[1,0],[2,0],[3,1],[3,2]]), [0,1,2,3]),
    ((1, []), [0]),
    ((3, [[0,1],[1,2],[2,0]]), []),
    ((6, [[1,0],[2,1],[3,1],[4,1],[3,2],[5,4],[5,3]]), [0,1,2,4,3,5]),
    ((8, [[1,0],[2,1],[3,1],[4,1],[3,2],[5,4],[5,3]]), [0,6,7,1,2,4,3,5]),
    ((6, [[1,0],[2,1],[3,1],[4,1],[3,2],[5,4],[1,5]]), []),
    ((8, [[1,0],[2,1],[3,1],[4,1],[3,2],[5,4],[1,5]]), []),
]
sol = Solution()
for inp, ans in cases:
    res = sol.findOrder(*inp)
    print(inp, res, ans)
