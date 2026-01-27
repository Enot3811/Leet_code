"""1109. Corporate Flight Bookings

https://leetcode.com/problems/corporate-flight-bookings/

There are n flights that are labeled from 1 to n.

You are given an array of flight bookings bookings,
where bookings[i] = [firsti, lasti, seatsi] represents a booking for flights firsti
through lasti (inclusive) with seatsi seats reserved for each flight in the range.

Return an array answer of length n, where answer[i] is the total number of seats
reserved for flight i. 

Example 1:
Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
Explanation:
Flight labels:        1   2   3   4   5
Booking 1 reserved:  10  10
Booking 2 reserved:      20  20
Booking 3 reserved:      25  25  25  25
Total seats:         10  55  45  25  25
Hence, answer = [10,55,45,25,25]

Example 2:
Input: bookings = [[1,2,10],[2,2,15]], n = 2
Output: [10,25]
Explanation:
Flight labels:        1   2
Booking 1 reserved:  10  10
Booking 2 reserved:      15
Total seats:         10  25
Hence, answer = [10,25]

Constraints:
1 <= n <= 2 * 10^4
1 <= bookings.length <= 2 * 10^4
bookings[i].length == 3
1 <= firsti <= lasti <= n
1 <= seatsi <= 10^4
"""

# Теги
# Префиксные суммы (prefix sums)

# Размышления
# На ум может прийти решение с сегментами, и оно может пройти, но будет не оптимальным.
# Интереснее подход с префиксными суммами.
# Создаём новый массив с нулями, по которому в конце будем считать префиксную сумму.
# Берём тройку l, r, n, и прибавляем n к l-му элементу.
# То есть все значения начиная с l получат +n.
# Но так как нам нужно, чтобы после r не получили, то r-му элементу отнимем n.
# И по итогу получится отрезок [l,r] на котором у префиксной суммы будет +n,
# а после обратно отнимется.
# Prefix_sum на i-м элементе и будет значением seats[i].

from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = [0] * n
        prefixes = [0] * (n + 1)
        for booking in bookings:
            prefixes[booking[0] - 1] += booking[2]
            prefixes[booking[1]] -= booking[2]
        prefix_sum = 0
        for i in range(n):
            prefix_sum += prefixes[i]
            seats[i] = prefix_sum
        return seats
        

cases = [
    (([[1,2,10]], 2), [10,10]),
    (([[1,2,10],[2,3,20],[2,5,25]], 5), [10,55,45,25,25]),
    (([[1,2,10],[2,2,15]], 2), [10,25]),
]
sol = Solution()
for inp, ans in cases:
    res = sol.corpFlightBookings(*inp)
    print(inp, res, ans)
