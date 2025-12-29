"""Fruit Into Baskets.

You are visiting a farm that has a single row of fruit trees arranged from left
to right. The trees are represented by an integer array fruits where fruits[i]
is the type of fruit the ith tree produces.

You want to collect as much fruit as possible.
However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type
of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit
from every tree (including the start tree) while moving to the right.
The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets,
you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].

Constraints:
1 <= fruits.length <= 10**5
0 <= fruits[i] < fruits.length
"""


from typing import List
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0

        max_fruits = 0
        fruits_types = defaultdict(int)
        n_types = 0
        cur_fruits = 0

        for fruit in fruits:
            
            # Если не было таких же, то такой тип ещё не собирался
            if fruits_types[fruit] == 0:
                
                n_types += 1
                
                # Тогда надо проверить сколько типов на данный момент
                if n_types > 2:
                    # Подводим итоги, сколько насчитали
                    max_fruits = max(max_fruits, cur_fruits)

                    # Удаляем из набранного фрукты, пока типов не станет меньше
                    while n_types > 2:
                        left_fruit = fruits[left]
                        fruits_types[left_fruit] -= 1
                        cur_fruits -= 1
                        if fruits_types[left_fruit] == 0:
                            n_types -= 1
                            del fruits_types[left_fruit]
                        left += 1

            # Текущий фрукт в любом случае считаем
            cur_fruits += 1
            fruits_types[fruit] += 1
        
        max_fruits = max(max_fruits, cur_fruits)
        return max_fruits


sol = Solution()
fruits = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]
print(sol.totalFruit(fruits))
