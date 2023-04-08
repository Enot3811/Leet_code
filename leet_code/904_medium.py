'''Fruit Into Baskets.'''


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
