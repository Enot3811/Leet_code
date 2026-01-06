"""309. Best Time to Buy and Sell Stock with Cooldown

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

You are given an array prices where prices[i]
is the price of a given stock on the ith day.

Find the maximum profit you can achieve.
You may complete as many transactions as you like (i.e., buy one and sell one share
of the stock multiple times) with the following restrictions:
- After you sell your stock, you cannot buy stock on the next day
(i.e., cooldown one day).
- Note: You may not engage in multiple transactions simultaneously
(i.e., you must sell the stock before you buy again). 

Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0

Constraints:
1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""

# Теги
# Продолжение задачи, Поиск в глубину (dfs), Мемоизация словарём (dict memoization),
# Конечный автомат (finite state machine)

# Размышления
# Продолжение серии задач про покупку/продажу 121, 122, 123.
# Наиболее похожей покажется 122, однако по решению ближе 123.
# У нас в каждый день будут выборы, несущие непонятные выгоды.
# Все их можно проверить с dfs. А для оптимизации использовать мемоизацию.
# В каждый день может быть всего 2 уникальных состояния.
# У нас либо есть акция, либо нет.
# То есть придётся посчитать 2n уникальных состояний, и это и будет временная сложность.
# Кулдаун можно не считать за уникальное состояние, а просто перематывать эти дни.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memory = {}  # (индекс, есть ли акция)

        def dfs(i: int, has_stock: bool) -> int:
            idx = (i, has_stock)
            if idx in memory:
                return memory[idx]
            if i >= len(prices):
                return 0
            # Если есть акция, то можем продать или ничего не делать
            if has_stock:
                memory[idx] = max(
                    dfs(i + 1, has_stock),
                    # Интересный момент, как можно обыграть кулдаун после продажи.
                    # Просто пропускаем следующий день, ведь всё равно ничего не можем
                    dfs(i + 2, not has_stock) + prices[i]
                )

            # Если нет, то можем купить, или ничего не делать
            else:
                memory[idx] = max(
                    dfs(i + 1, has_stock),
                    dfs(i + 1, not has_stock) - prices[i]
                )
            return memory[idx]
        return dfs(0, False)

# Иной более эффективный вариант решения - конечный автомат.
# Для решения необходимо определиться какие есть состояния
# и как они переходят друг в друга.
# Состояния:
# hold - у нас есть акция, мы готовы её продать
# sold - мы продали акцию и не можем купить из-за кулдауна
# rest - у нас нет акции и мы ничего не делаем
# Переходы:
# В hold мы можем попасть если:
# 1) Мы уже держим акцию (hold)
# 2) Мы не держим акцию (rest) и покупаем сегодня (price)
# В sold мы можем попасть если:
# 1) Мы держим акцию (hold) и продаём сегодня (price)
# В rest мы можем попасть если:
# 1) Мы продали акцию вчера (sold)
# 2) Мы просто сидим (rest)
# И в итоге мы каждый день выбираем лучшее из всех состояний.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        hold = float("-inf")  # Так как невозможно держать акцию до торгов
        sold = 0  # Ничего не заработали
        rest = 0  # Денег нет

        for price in prices:
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            # Или уже держим, или покупаем сегодня
            hold = max(prev_hold, prev_rest - price)
            # Продать можем только если холдили
            sold = prev_hold + price
            # Быть без акции можем если продали вчера или просто сидим
            rest = max(prev_sold, prev_rest)
        
        # Выбираем лучшее из всех состояний. Hold не выгоден, ведь акцию лучше продать
        return max(sold, rest)


cases = [
    ([7, 1, 3, 4, 0, 2, 3], 5),
    ([7, 1, 3, 6, 0, 2, 3], 6),
    ([0], 0),
    ([1,3,5,2,6,0,4,6], 10),
    ([5,4,3,2,1], 0),
]
sol = Solution()
for prices, ans in cases:
    res = sol.maxProfit(prices)
    print(prices, res, ans)
