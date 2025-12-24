"""A. Префиксные суммы

https://contest.yandex.ru/contest/66793/problems/A/

По данной последовательности a1,a2,…,an вычислите последовательность ее префиксных сумм
b1,b2,…,bn, где bj=∑ai.

Формат ввода
В первой строке дано целое число 1≤n≤10^3 — количество элементов в последовательности a.
Во второй строке дано 
n целых чисел a1,a2,…,an (|ai|≤10^6) — элементы последовательности.

Формат вывода:
Выведите n целых чисел b1,b2,…,bn — последовательность префиксных сумм
для последовательности a.

Пример
Ввод
5
10 -4 5 0 2
Вывод
10 6 11 11 13 
"""


def prefix_sum(arr: list[int]) -> list[int]:
    prefix_sum = [0] * len(arr)
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        prefix_sum[i] = cur_sum
    return prefix_sum

n = int(input())
arr = list(map(int, input().split()))

print(*prefix_sum(arr))

examples = [
    ([1, 2, 3, 4, 5], [1, 3, 6, 10, 15]),
    ([10, -4, 5, 0, 2], [10, 6, 11, 11, 13]),
    ([0], [0]),
]

for arr, expected in examples:
    print(arr, prefix_sum(arr), expected)
