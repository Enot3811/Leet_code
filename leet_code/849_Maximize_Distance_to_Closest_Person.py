"""849. Maximize Distance to Closest Person

https://leetcode.com/problems/maximize-distance-to-closest-person/

You are given an array representing a row of seats where seats[i] = 1 represents
a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat
is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and
the closest person to him is maximized. 

Return that maximum distance to the closest person.

Example 1:
Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]),
then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

Example 2:
Input: seats = [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.

Example 3:
Input: seats = [0,1]
Output: 1

Constraints:
2 <= seats.length <= 2 * 10^4
seats[i] is 0 or 1.
At least one seat is empty.
At least one seat is occupied.
"""

# Теги
# Плавающее окно (left-right pointers)

# Размышления
# Классическая задача на плавающее окно.
# Оставляем первый указатель там, где встретили 1, и расширяем окно до тех пор,
# пока снова не встретили 1.
# После чего дистанция делится пополам, левый указатель сдвигается на новую 1.
# Из интересного - расположение по краям.
# Если обычно размещаемся между людей и пытаемся сесть равноудалённо,
# то по краям мы просто садимся на самый край, максимально удаляясь от соседа.

from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left = -1
        max_dist = 0
        for right, seat in enumerate(seats):
            if seat == 1:
                # Если пустые места с левого края
                if left == -1:
                    max_dist = max(max_dist, right)
                # Места между двумя людьми
                else:
                    max_dist = max(max_dist, (right - left) // 2)
                left = right
        # Места с правого края
        max_dist = max(max_dist, right - left)
        return max_dist

cases = [
    ([1,0,0,0,1,0,1], 2),
    ([1,1,0], 1),
    ([0,0,1,1], 2),
    ([0,1,0,0], 2),
    ([1,0,0,1], 1),
    ([0,1,0,1,0,1,0], 1),
    ([0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0], 4),
    ([0,0,0,1,0,1,0,0,0,0,0,0,1,0,0], 3),
    ([1,1,1,1,1,0,1,1,1], 1),
    ([0,0,0,0,0,1,0,0,0,0], 5),
    ([0,0,0,0,0,1], 5),
    ([1,0,0,0,0,0], 5),
]
sol = Solution()
for seats, ans in cases:
    res = sol.maxDistToClosest(seats)
    print(seats, res, ans)
