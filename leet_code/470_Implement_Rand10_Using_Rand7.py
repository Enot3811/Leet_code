"""470. Implement Rand10() Using Rand7()

https://leetcode.com/problems/implement-rand10-using-rand7/

Given the API rand7() that generates a uniform random integer in the range [1, 7],
write a function rand10() that generates a uniform random integer in the range [1, 10].
You can only call the API rand7(), and you shouldn't call any other API.
Please do not use a language's built-in random API.

Each test case will have one internal argument n, the number of times
that your implemented function rand10() will be called while testing.
Note that this is not an argument passed to rand10().

Example 1:
Input: n = 1
Output: [2]

Example 2:
Input: n = 2
Output: [2,8]

Example 3:
Input: n = 3
Output: [3,8,10]

Constraints:
1 <= n <= 10^5

Follow up:
What is the expected value for the number of calls to rand7() function?
Could you minimize the number of calls to rand7()?
"""

# Теги
# Задача со сложной уникальной идеей

# Размышления
# Здесь используется техника rejection sampling.
# Она основана на нескольких идеях:
# 1) Если бы у нас был кубик с 6 гранями, а нам нужно было бы 5, то мы могли бы просто
# продолжить пользоваться текущим кубиком, игнорируя выпадение 6.
# Ведь все варианты равновероятны.
# 2) Если бы нам нужно было больше 6 вариантов, то мы могли бы использовать два кубика.
# При этом сделать так, что первый кубик давал бы числа с шагом 6, а второй с шагом в 1.
# Получается первый дал бы значения 0, 7, 13, 19, 25, 31, а второй 0, 1, 2, 3, 4, 5,
# и суммируя их мы бы получили 36 равновероятных вариантов.
# И далее можно применить первое правило. Если нам нужно например 10, то мы можем просто
# отрезать всё, что больше 10 и перебрасывать.
# Но здесь появляется проблема, что придётся довольно много перебрасывать.
# Тогда отрежем до 30, а затем сделаем %10. Тогда мы ужмёмся в 10 различных исходов,
# каждый из которых может появиться 3 разными способами.
# Но при этом они все равновероятны.
# Важно, чтобы при % мы брали кратное число. То есть если бы оставили 36 % 10, то
# у значений от 0 до 6 было бы 4 варианта появления, а у 7-10 всего 3.
# Вся эта логика применяется здесь, но уже на 7 и 10.

from random import randint

def rand7():
    return randint(1, 7)

class Solution:
    def rand10(self):
        i = rand7() - 1
        j = rand7() - 1
        x = i * 7 + j
        if x >= 40:
            return self.rand10()
        return x % 10 + 1

sol = Solution()
counter = {}
for i in range(1, 11):
    counter[i] = 0
for _ in range(1000000):
    counter[sol.rand10()] += 1
print(counter)
