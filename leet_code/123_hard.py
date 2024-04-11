"""
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

from typing import List

# Iteration 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = self.make_step(prices, 0, 0, 0, False)
        return profit
    
    def make_step(
        self, prices: List[int], i: int, current_profit: int,
        transaction_cnt: int, have_stock: bool
    ) -> int:
        # Если уже проведены 2 транзакции, то можем возвращать полученную
        # прибыль
        if transaction_cnt == 2:
            return current_profit
        # Если прошли все элементы, то возвращаем получившуюся прибыль
        if i >= len(prices):
            return current_profit

        # Если есть акция, то можем решать о продаже
        if have_stock:
            # Выбираем тот сценарий, который принесёт больше прибыли
            current_profit = max(
                # Продали акцию, увеличили профит, нарастили счётчик транзакций
                self.make_step(prices, i + 1, current_profit + prices[i],
                               transaction_cnt + 1, have_stock=False),
                # Не продали акцию, просто перешли к следующему элементу
                self.make_step(prices, i + 1, current_profit,
                               transaction_cnt, have_stock=True)
            )
        # Если нет акции, то решаем о покупке
        else:
            # Выбираем тот сценарий, который принесёт больше прибыли
            current_profit = max(
                # Купили акцию, уменьшили профит на потраченные средства
                self.make_step(prices, i + 1, current_profit - prices[i],
                               transaction_cnt, have_stock=True),
                # Не купили акцию, просто перешли к следующему элементу
                self.make_step(prices, i + 1, current_profit,
                               transaction_cnt, have_stock=False)
            )
        # В итоге после проверки ветвей у нас окажется максимальный профит
        # для текущего элемента
        return current_profit


# Iteration 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Память для всех элементов
        # Придётся хранить оптимальное значение не просто для каждого i-го,
        # но и для всех его вариаций
        # Придя к i-му элементу мы можем иметь разные условия,
        # а именно количество потраченных транзакций, и держим ли мы сейчас
        # акцию, или нет
        # Ключ словаря будет вида (i, transaction_cnt, have_stock)
        self.memory = {}
        profit = self.make_step(prices, 0, 0, False)
        return profit
    
    def make_step(
        self, prices: List[int], i: int,
        transaction_cnt: int, have_stock: bool
    ) -> int:
        # Собираем текущий случай из входных данных и проверяем, был ли он
        current_case = (i, transaction_cnt, have_stock)
        if current_case in self.memory:
            return self.memory[current_case]

        # Если уже проведены 2 транзакции, или прошли все элементы,
        # то сейчас уже не получим никакой прибыли
        if transaction_cnt == 2 or i >= len(prices):
            return 0

        # Если есть акция, то можем решать о продаже
        if have_stock:
            # Выбираем тот сценарий, который принесёт больше прибыли
            current_profit = max(
                # То, что мы получим потом, + текущая продажа
                prices[i] + self.make_step(
                    prices, i + 1, transaction_cnt + 1, have_stock=False),
                # Или просто то, что получим потом без продажи
                self.make_step(
                    prices, i + 1, transaction_cnt, have_stock=True)
            )
        # Если нет акции, то решаем о покупке
        else:
            # Выбираем тот сценарий, который принесёт больше прибыли
            current_profit = max(
                # То, что получим потом, - текущая покупка
                self.make_step(
                    prices, i + 1, transaction_cnt, have_stock=True
                ) - prices[i],
                # Или просто то, что получим потом без покупки
                self.make_step(
                    prices, i + 1, transaction_cnt, have_stock=False)
            )
        # В итоге после проверки ветвей у нас окажется максимальный профит
        # для текущего элемента
        self.memory[current_case] = current_profit
        return current_profit


# Iteration 3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.memory = {}
        profit = self.make_step(prices, 0, 0, False)
        return profit
    
    def make_step(
        self, prices: List[int], i: int,
        transaction_cnt: int, have_stock: bool
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

# Someone else's decision
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, sell1, buy2, sell2 = float('-inf'), 0, float('-inf'), 0
        for price in prices:
            # Update buy1 to reflect the maximum of not buying
            # or buying the stock at the current price
            buy1 = max(buy1, -price)
            # Update sell1 to reflect the maximum of not selling
            # or selling the stock bought at buy1 price
            sell1 = max(sell1, buy1 + price)
            # Update buy2 to reflect the maximum of not buying the second stock
            # or buying the stock at the current price minus the profit
            # from the first sell
            buy2 = max(buy2, sell1 - price)
            # Update sell2 to reflect the maximum of not selling the second
            # stock or selling the stock bought at buy2 price
            sell2 = max(sell2, buy2 + price)
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
