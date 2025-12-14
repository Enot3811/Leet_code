"""121. Best Time to Buy and Sell Stock

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock
on the i-th day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed
because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 
Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""

# Размышления
# На каждом шаге мы можем проверять текущий минимум и максимум.
# Если нашли новый максимум - хорошо, ответ станет больше.
# Если нашли новый минимум, то мы уже не сможем использовать старый максимум.
# Нужно посчитать ответ с его участием и теперь искать новый максимум.
# В итоге линейный проход по массиву.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = prices[0]
        best_sell = None
        best_profit = 0
        for i in range(1, len(prices)):
            # Всегда ищем продажу подороже
            if best_sell is None or best_sell < prices[i]:
                best_sell = prices[i]
                

            if best_buy > prices[i]:  # Всегда ищем покупку подешевле
                
                # Если нашли другую покупку, то надо подытожить старую
                if best_sell is not None:
                    current_profit = best_sell - best_buy

                    if best_profit < current_profit:
                        best_profit = current_profit
                best_buy = prices[i]
                best_sell = None

        # Проверка напоследок
        if best_sell is not None:
            current_profit = best_sell - best_buy
            if best_profit < current_profit:
                best_profit = current_profit
        return best_profit
    

# Более короткое решение, но по эффективности +- так же
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         best_buy = float('inf')
#         best_profit = 0
#         for price in prices:
#             best_buy = min(best_buy, price)  # Всегда ищем покупку подешевле

#             curr_profit = price - best_buy  # Выгода с текущей продажей
#             # В итоге минимум сдвигается,
#             # а максимум проверяется каждую итерацию
#             best_profit = max(best_profit, curr_profit)
#         return best_profit
    

if __name__ == '__main__':
    cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([3, 5, 2, 1, 5, 1000, 5000], 4999),
        ([5000, 50, 100, 2, 30, 31, 1], 50),
        ([5, 5, 5, 5], 0),
        ([5], 0),
        ([5000, 1], 0),
        ([5000, 1, 4, 4, 4, 4], 3),
        ([5000, 1, 4, 5, 6, 7, 1], 6),
        ([1, 4, 5, 6, 7, 2, 8, 2, 9, 2, 8, 2, 7, 1], 8),
        ([0, 0, 0, 1], 1),
        ([0, 0, 0, 0], 0),
        ([1, 0], 0)
    ]
    sol = Solution()
    for inp, ans in cases:
        out = sol.maxProfit(inp)
        print('ans:', out, 'exp:', ans)
