"""1011. Capacity To Ship Packages Within D Days

https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

A conveyor belt has packages that must be shipped from one port
to another within `days` days.

The i-th package on the conveyor belt has a weight of `weights[i]`.
Each day, we load the ship with packages on the conveyor belt
(in the order given by weights).
We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages
on the conveyor belt being shipped within days days.

Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages
in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
Note that the cargo must be shipped in the order given, so using a ship of capacity 14
and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10)
is not allowed.

Example 2:
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages
in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Example 3:
Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1

Constraints:
1 <= days <= weights.length <= 5 * 10^4
1 <= weights[i] <= 500
"""

# Теги
# Бинарный поиск (Binary Search)

# Размышления
# В этой задаче сразу хочется закопаться в лоб в рекурсивное решение.
# То есть можно поразмыслить и увидеть, что нам нужно подобрать `days` отрезков так,
# чтобы получить минимальный максимум их сумм.
# Не знаю как, но очень важно посмотреть на задачу с другой стороны.
# Особенно учитывая, что есть очень скромный constrain на weights[i] относительно длины.
# Мы можем зафиксировать capacity и проверить с ней, получится ли перевести товары.
# Если не получится, то увеличиваем и пробуем ещё раз.
# В итоге что-то около n^2, хотя на самом деле больше.
# Но в любом случае, нас же не принуждают инкрементировать capacity.
# Можем прибавлять что-то другое, побольше.
# Или же воспользоваться бинарным поиском.
# Ведь нам нужно найти подходящее число. При этом минимальное подходящее число.
# За max возьмём сумму всех грузов. За min максимальный вес из имеющихся.

def find_ship_capacity(weights: list[int], days: int) -> int:

    def check_capacity(capacity: int):
        curr_sum = 0
        remain_days = days
        for weight in weights:
            # Если нет, то смотрим, помещается ли он
            curr_sum += weight
            if curr_sum > capacity:
                remain_days -= 1
                # Если мы истратили последний день
                if remain_days == 0:
                    return False
                # Иначе грузим груз в новый рейс и продолжаем
                curr_sum = weight
        return True

    if not weights:
        return 0
    min_capacity = max(weights)
    max_capacity = sum(weights)

    while min_capacity < max_capacity:

        curr_capacity = (min_capacity + max_capacity) // 2

        if check_capacity(curr_capacity):
            max_capacity = curr_capacity
        else:
            min_capacity = curr_capacity + 1
    return min_capacity