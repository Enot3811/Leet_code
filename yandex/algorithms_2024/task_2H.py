"""H. Переезд в опенспейс

Есть кабинеты, расположенные в линию, и в каждом из них ai сотрудников.
Необходимо перевести всех сотрудников в один из кабинетов.
И так как кабинеты в линию, то переезды проходят вдоль всех кабинетов.
Например [1, 0, 0]. Чтобы перевести этого сотрудника направо, нужно 2 переезда.

Задача - есть какой-то оптимальный кабинет, при переселении в который будет произведено
минимальное количество переездов. Необходимо найти это оптимальное количество.
"""


def find_optimum_migrations(arr: list[int]) -> int:
    # Посчитаем кумулятивную сумму переездов слева-направо и справа-налево
    left_right = [0] * len(arr)
    right_left = [0] * len(arr)
    employers_to_go = 0
    for i in range(len(arr)):
        left_right[i] = employers_to_go + (0 if i == 0 else left_right[i - 1])
        employers_to_go += arr[i]
    employers_to_go = 0
    for i in range(len(arr) - 1, -1, -1):
        right_left[i] = employers_to_go + (0 if i == len(arr) - 1 else right_left[i + 1])
        employers_to_go += arr[i]
    # Теперь ищем, где сумма переездов справа налево и слева-направо будет минимальной
    return min(map(lambda x: sum(x), zip(left_right, right_left)))

_ = input()
arr = list(map(int, input().split()))
print(find_optimum_migrations(arr))

# examples = [
#     ((4, [5, 2, 3, 1]), 10),
#     ((5, [5, 4, 3, 2, 1]), 15)
# ]

# for inp, ans in examples:
#     _, arr = inp
#     res = find_optimum_migrations(arr)
#     print(arr, res, ans)
