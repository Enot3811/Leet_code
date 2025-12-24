"""F. Сумма тройных произведений

https://contest.yandex.ru/contest/66793/problems/F/

Есть массив чисел a_i длиной n.
Нужно посчитать сумму произведений троек чисел a_i * a_j * a_k
для всех i, j, k от 0 до n-1.

Так как ответ может быть большим, нужно посчитать ответ по модулю 10^9 + 7.
"""


# Размышления
# Можем зафиксировать j-й элемент.
# Чтобы посчитать сумму произведений троек троек у нас получается формула
# aj * (a0 * aj+1 + a0 * aj+2 + ...)
# Выносим a0: aj * a0 * (sum(aj+1, ..., an))
# Но при этом и a0 перебирается a0, a1, ..., aj-1. Тоже вынесем
# aj * sum(aj+1, ..., an) * sum(a0, ..., aj-1)


MOD = 1000000007

def sum_all_products(arr: list[int]) -> int:
    n = len(arr)
    # Посчитаем суммы слева-направо и справа-налево
    left_right_sum = [0] * n
    right_left_sum = [0] * n

    left_right_sum[0] = arr[0] % MOD  # операции с большими числами - медленные.
    # Но при этом деление с остатком можно внести в скобки, и это не повлияет
    # на итоговый результат
    for i in range(1, n):
        left_right_sum[i] = (arr[i] + left_right_sum[i - 1]) % MOD

    right_left_sum[-1] = arr[-1] % MOD
    for i in range(n - 2, -1, -1):
        right_left_sum[i] = (arr[i] + right_left_sum[i + 1]) % MOD

    # Теперь проходим j индексом, пользуясь суммами справа и слева
    result = 0
    for j in range(1, n - 1):
        result = (result + arr[j] * left_right_sum[j - 1] * right_left_sum[j + 1]) % MOD
    return result


def test(arr: list[int]) -> int:
    """Функция для тестов"""
    result = 0
    for i in range(0, len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                result += arr[i] * arr[j] * arr[k]
    return result


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(sum_all_products(arr))


# if __name__ == "__main__":
#     examples = [
#         (4, [0, 5, 6, 7]),
#         (3, [1, 2, 3]),
#         (10, [5, 1, 7, 2, 4, 2, 8, 1, 4, 9])
#     ]

#     for example in examples:
#         _, arr = example
#         res = test(arr)
#         ans = sum_all_products(arr)
#         print(arr, ans, res)
    