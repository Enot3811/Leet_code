"""123. Best Time to Buy and Sell Stock III

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

You are given an array prices where prices[i]
is the price of a given stock on the ith day.

Find the maximum profit you can achieve.
You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously
(i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3),
profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5),
profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later,
as you are engaging multiple transactions at the same time.
You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^5
"""

# Теги
# Поиск в глубину (dfs), Продолжение задачи, Конечный автомат (finite state machine)

# Размышления
# Продолжение задач 121 и 122 про выгодную продажу акций.
# В предыдущей задаче можно было сколько угодно раз покупать и продавать,
# чтобы получить наибольшую прибыль.
# Здесь же можно сделать лишь 2 покупки и продажи.
# Если у нас есть несколько подъёмов и спусков, на которых мы можем купить и продать,
# то всегда выгодно купить в начале всех спусков, и продать в конце, вместо того,
# чтобы купить в начале 1-го, и продать в конце последнего.
# Например: 1,5,3,6,3,7. 3 подъёма. Можно слить их, купив за 1, продав за 7,
# но это хуже, чем купить 1, 3 и 3, и продать 5, 6 и 7.
# Ограничение накладывает лишь условие задачи. Мы не можем купить 3 раза.
# Потому нам придётся сливать интервалы воедино.
# Купить за 1, продать за 6, купить за 3, продать за 7 оптимальное решение,
# при возможности купить лишь 2 раза.
# Можно решить эту задачу в лоб с помощью dfs.
# Просто перебираем все варианты, когда мы можем купить или продать.
# При этом можно унаследовать решение прошлой задачи и делать ветвление только в конце
# и начале интервалов.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.memory = {}
        profit = self.make_step(prices, 0, 0, False)
        return profit
    
    def make_step(
        self,
        prices: List[int],
        i: int,
        transaction_cnt: int,
        have_stock: bool
    ) -> int:
        current_case = (i, transaction_cnt, have_stock)
        if current_case in self.memory:
            return self.memory[current_case]

        if transaction_cnt == 2 or i >= len(prices):
            return 0

        # Если есть акция, то можем решать о продаже
        if have_stock:
            # Добавляем логику из прошлой задачи
            # Если у нас сейчас есть акция и мы на подъёме,
            # то нет смысла продавать её сейчас, поэтому просто пойдём дальше
            # к большему значению
            if i < len(prices) - 1 and prices[i + 1] >= prices[i]:
                current_profit = self.make_step(
                    prices, i + 1, transaction_cnt, have_stock=True)
            else:
                current_profit = max(
                    prices[i] + self.make_step(
                        prices, i + 1, transaction_cnt + 1, have_stock=False),
                    self.make_step(
                        prices, i + 1, transaction_cnt, have_stock=True)
                )
        # Если нет акции, то решаем о покупке
        else:
            # Если у нас нет акции и мы на спуске, то нет смысла покупать её
            # сейчас. Просто перейдём к следующей итерации
            if i < len(prices) - 1 and prices[i + 1] <= prices[i]:
                current_profit = self.make_step(
                    prices, i + 1, transaction_cnt, have_stock=False)
            else:
                current_profit = max(
                    self.make_step(
                        prices, i + 1, transaction_cnt, have_stock=True
                    ) - prices[i],
                    self.make_step(
                        prices, i + 1, transaction_cnt, have_stock=False)
                )

        self.memory[current_case] = current_profit
        return current_profit

# Второе решение основано на конечном автомате.
# Для решения необходимо определиться какие есть состояния
# и как они переходят друг в друга.
# Состояния:
# buy1 - мы купили акцию первый раз, и можем её продать
# sell1 - мы продали акцию первый раз, и можем её купить снова
# buy2 - мы купили акцию второй раз, и можем её продать
# sell2 - мы продали акцию второй раз, и можем её купить снова
# Переходы:
# В buy1 мы можем попасть если:
# 1) Мы уже купили акцию (buy1)
# 2) Мы можем купить сегодня (price)
# В sell1 мы можем попасть если:
# 1) Мы уже продали акцию (sell1) и ничего не делаем
# 2) Мы купили акцию (buy1) и продали сегодня (price)
# В buy2 мы можем попасть если:
# 1) Мы уже купили акцию (buy2)
# 2) Мы продали акцию (sell1) и купили её снова (price)
# В sell2 мы можем попасть если:
# 1) Мы уже продали акцию (sell2) и ничего не делаем
# 2) Мы купили акцию (buy2) и продали сегодня (price)
# И в итоге мы каждый день выбираем лучшее из всех состояний.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, sell1, buy2, sell2 = float('-inf'), 0, float('-inf'), 0
        for price in prices:
            # Пытаемся купить дешевле, или не покупаем
            buy1 = max(buy1, -price)
            # Пытаемся продать выгоднее
            sell1 = max(sell1, buy1 + price)
            # После первой продажи снова пытаемся купить подешевле,
            # но при этом держим в уме уже полученную выгоду sell1
            buy2 = max(buy2, sell1 - price)
            # Стараемся выгоднее продать второй раз, или оставляем старый вариант
            sell2 = max(sell2, buy2 + price)
        # Итог после двух операций
        return sell2


if __name__ == '__main__':
    cases = [
        ([7, 1, 5, 3, 6, 4], 7),
        ([7, 6, 4, 3, 1], 0),
        ([1, 5, 4000, 5000], 4999),
        ([1, 10, 2, 20], 27),
        ([3, 2, 1, 5, 6], 5),
        ([1, 3, 5, 7, 4, 3, 8, 10, 7, 20, 19, 18], 23),
        ([1, 3, 5, 7, 5, 8], 9),
        ([0], 0),
        ([1, 9, 4, 13, 20, 25, 0, 30], 54),
        ([25, 40, 0, 10, 5, 4, 10], 25),
        ([5, 2, 3, 10, 13, 5, 2, 5, 7, 9, 1, 4, 2, 6, 11, 32, 22, 44, 13, 1, 5,
          8, 23, 11, 55, 1, 0, 10, 1], 97)
    ]
    sol = Solution()
    for inp, ans in cases:
        out = sol.maxProfit(inp)
        print('ans:', out, 'exp:', ans)
