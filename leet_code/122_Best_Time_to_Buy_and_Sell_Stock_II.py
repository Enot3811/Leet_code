"""122. Best Time to Buy and Sell Stock II

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

You are given an integer array prices
where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5),
profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5),
profit = 5-1 = 4.
Total profit is 4.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit,
so we never buy the stock to achieve the maximum profit of 0.
 
Constraints:
1 <= prices.length <= 3 * 10^4
0 <= prices[i] <= 10^4
"""

# Теги
# Продолжение задачи

# Размышления
# Задача является продолжением задачи (121. Best Time to Buy and Sell Stock).
# Отличие в том, что там искали одну оптимальную покупку и продажу, а здесь все.
# То есть если мы можем купить дешевле и продать дороже, то это надо делать.
# В итоге покрываем все восходящие промежутки.
# Если число больше предыдущего, то холдим.
# Если число меньше, то продаём на предыдущем и покупаем на текущем.
# Если уменьшение продолжается, то продастся там же, где и купилось, то есть 0 потерь.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        whole_profit = 0
        current_profit = 0  # Профит от текущего восходящего тренда
        best_buy = prices[0]
        for price in prices:
            this_profit = price - best_buy
            # Профит обновится, если цена выше предыдущей
            if current_profit <= this_profit:
                current_profit = this_profit
            # Иначе мы уже достигли пика на прошлом шаге
            else:
                whole_profit += current_profit
                current_profit = 0
                best_buy = price  # Делаем новую покупку каждый раз
                # когда цена оказалась меньше предыдущей
                # (то есть профит оказался меньше)
        whole_profit += current_profit
        return whole_profit
    

if __name__ == '__main__':
    cases = [
        ([7, 1, 5, 3, 6, 4], 7),
        ([7, 6, 4, 3, 1], 0),
        ([1, 5, 4000, 5000], 4999),
        ([1, 10, 2, 20], 27),
        ([3, 2, 1, 5, 6], 5),
        ([1, 3, 5, 7, 4, 3, 8, 10, 7, 20, 19, 18], 26),
        ([1, 3, 5, 7, 5, 8], 9),
        ([0], 0)
    ]
    sol = Solution()
    for inp, ans in cases:
        out = sol.maxProfit(inp)
        print('ans:', out, 'exp:', ans)
