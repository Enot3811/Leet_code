"""2013. Detect Squares

Check the images!
https://leetcode.com/problems/detect-squares/

You are given a stream of points on the X-Y plane. Design an algorithm that:
- Adds new points from the stream into a data structure.
Duplicate points are allowed and should be treated as different points.
- Given a query point, counts the number of ways to choose three points
from the data structure such that the three points and the query point
form an axis-aligned square with positive area.

An axis-aligned square is a square whose edges are all the same length
and are either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:
- DetectSquares() Initializes the object with an empty data structure.
- void add(int[] point) Adds a new point point = [x, y] to the data structure.
- int count(int[] point) Counts the number of ways to form axis-aligned squares
with point point = [x, y] as described above.
 
Example 1:
Input
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
Output
[null, null, null, null, 1, 0, null, 2]

Explanation
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // return 1. You can choose:
                               //   - The first, second, and third points
detectSquares.count([14, 8]);
// return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
detectSquares.count([11, 10]); // return 2. You can choose:
                               //   - The first, second, and third points
                               //   - The first, third, and fourth points

Constraints:
point.length == 2
0 <= x, y <= 1000
At most 3000 calls in total will be made to add and count.
"""

# Размышления
# Так как границы x и y относительно небольшие,
# можно позволить хранить дикт со всеми осями.
# Например, есть точка (2,5).
# Тогда у нас получится структура {2: {5: 1}}, где первый дикт хранит оси 'y',
# второй 'x' координаты на этой оси и количество точек с этой координатой.
# Как будем искать точки для квадрата:
# - Подбираем точку pt1 на одной оси 'y' с заданной точкой.
# У неё та же 'y' координата, но иной 'x' (x, y_pt).
# - Вычисляем размер стороны (x_pt - x)
# - Можем отложить две параллельный стороны к полученной (y_pt - dx) и (y_pt + dx)
# - На этих параллелях 'y' ищем 'x' и x_pt

from typing import List

class DetectSquares:

    def __init__(self):
        # Содержит номера присутствующих y осей, которые хранят x оси.
        # А x оси хранят координату и счётчик точек с этой координатой.
        # В итоге получается комбинация (y, x, n)
        self.axes = {}

    def add(self, point: List[int]) -> None:
        x, y = point
        if y in self.axes:
            if x in self.axes[y]:
                self.axes[y][x] += 1
            else:
                self.axes[y][x] = 1
        else:
            self.axes[y] = {x: 1}
        
    def count(self, point: List[int]) -> int:
        x_pt, y_pt = point
        ans = 0

        # Проходим по всем x координатам с такой же y
        y_axis = self.axes.get(y_pt)
        if y_axis:
            for x, n_pt1 in y_axis.items():
                # Пропускаем вырожденные квадраты
                if x == x_pt:
                    continue

                dx = x_pt - x  # Смотрим насколько сдвигается точка по x
                
                # Находим 'y' параллели на том же расстоянии,
                # что и pt1 по 'x' от заданной точки
                for y in [y_pt + dx, y_pt - dx]:
                    x_axis = self.axes.get(y)
                    if x_axis:
                        n_pt2 = x_axis.get(x_pt, 0)
                        n_pt3 = x_axis.get(x, 0)
                        ans += n_pt1 * n_pt2 * n_pt3
        return ans


obj = DetectSquares()
print(obj.count([0,0]))  # 0
obj.add([3,10])
obj.add([11,2])
obj.add([3,2])
print(obj.count([11,10]))  # 1
print(obj.count([14,8]))  # 0
obj.add([11,2])
print(obj.count([11,10]))  # 2
obj.add([13,10])
obj.add([13,12])
print(obj.count([11,10]))  # 2
obj.add([11,12])
print(obj.count([11,10]))  # 3
obj.add([8,10])
obj.add([8,7])
obj.add([11,7])
print(obj.count([11,10]))  # 4
obj.add([11,10])
print(obj.count([11,10]))  # 4
obj.add([19,10])
obj.add([11,18])
obj.add([19,18])
print(obj.count([11,10]))  # 5
