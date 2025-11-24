"""322. Coin Change

https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 2**31 - 1
0 <= amount <= 10**4
"""

# Размышления
# Как оказалось, у данной задачи нет какого-то хитрого решения, которое бы избежало
# цикла по amount.
# Два базовых подхода: DFS с кэшем, или DP с таблицей.
# И тот и другой требует amount памяти,
# так как для каждого значения надо хранить оптимум.
# И сложность amount * len(coins), так как в общем случае надо решить задачу для каждого
# возможного числа взятием каждой монеты.


from typing import List, Optional

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memory = {0: 0}

        def step(remind: int) -> Optional[int]:
            if remind in memory:
                return memory[remind]
            if remind < 0:
                return -1

            optimum = -1
            for coin in coins:
                # Решаем подзадачу, когда взяли одну из монет
                new_solution = step(remind - coin)

                if optimum == -1 or new_solution != -1 and new_solution < optimum:
                    optimum = new_solution

            # Прибавляем текущую одну монету, но только если есть решение
            if optimum != -1:
                optimum += 1

            memory[remind] = optimum
            return memory[remind]
        
        return step(amount)

# DP здесь не очень интуитивный
# Мы пойдём по всем числам от 0 до amount и будем считать сколько монет нужно,
# чтобы к нему прийти.
# Чтобы найти оптимальные варианты, на каждом curr_amount придётся вычислять для всех
# монет.
# Как считаем: отступим от curr_amount назад на coin - это то, откуда мы можем добавить
# текущую монету. Там уже будет посчитано значение. Берём его и +1 текущая монета.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Заполняем таблицу невозможными значениями
        # Худший вариант, что монета = 1, значит шагов не может быть больше amount
        memory = [amount + 1] * (amount + 1)
        memory[0] = 0

        for curr_amount in range(1, amount + 1):
            for coin in coins:
                # Из какого количества мы можем прийти текущей монетой
                prev_amount = curr_amount - coin
                # Если такое количество вообще есть
                if prev_amount >= 0:
                    memory[curr_amount] = min(
                        memory[curr_amount],
                        memory[prev_amount] + 1
                    )
        return memory[amount] if memory[amount] != amount + 1 else -1


sol = Solution()
cases = [
    (([1,2,5], 11), 3),
    (([3], 2), -1),
    (([1], 0), 0),
    (([2,7],15), 5),
    (([1,2,7], 15), 3),
    (([2,3], 19), 7),
    (([2,4], 13), -1),
    (([2,4,6,8], 111), -1)
]
for inp, ans in cases:
    res = sol.coinChange(*inp)
    print(inp, res, ans)
