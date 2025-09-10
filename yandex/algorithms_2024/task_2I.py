"""I. Изучение алгоритмов

Есть список алгоритмов, которые нужно изучить.
Они характеризуются двумя характеристиками: интересность (массив а) и полезность (b).
Алгоритмы изучаются согласно настроению (массив p), где pi = 0 - изучается самый
интересный из оставшихся, а pi = 1 - самый полезный.
Если осталось несколько одинаковых по интересности/полезности, то выбирается тот,
у которого больше вторая характеристика. Если и вторая характеристика одинаковая, то
берётся тот, у кого меньше индекс

Необходимо найти правильный порядок изучения алгоритмов с характеристиками a и b, и
настроениями p.
"""

# Размышления
# Мы можем сделать аргсорт для a и b, получив порядок для интересных и полезных
# При вычёркивания элемента из одного из массивов мы можем запоминать индексы,
# и при совпадении индекса в другом массиве с уже вычеркнутым, мы просто пойдём дальше

def find_correct_study_order(a: list[int], b: list[int], p: list[int]) -> list[int]:
    arr_a = [(a[i], b[i], i) for i in range(len(a))]
    arr_b = arr_a[:]
    # Сортируем так, чтобы шла сначала основная характеристика, потом вторая,
    # и уже напоследок индекс
    arr_a = sorted(arr_a, reverse=True, key=lambda x: (x[0], x[1], -x[2]))
    arr_b = sorted(arr_b, reverse=True, key=lambda x: (x[1], x[0], -x[2]))

    # Проходим, вычёркиваем, запоминаем, формируем ответ
    answer = []
    popped = set()
    a_idx = 0
    b_idx = 0
    mood_idx = 0
    while mood_idx < len(p):
        if p[mood_idx] == 0:
            idx = arr_a[a_idx][2]
            if idx not in popped:
                popped.add(idx)
                answer.append(idx + 1)
                mood_idx += 1
            a_idx += 1
        else:
            idx = arr_b[b_idx][2]
            if idx not in popped:
                popped.add(idx)
                answer.append(idx + 1)
                mood_idx += 1
            b_idx += 1
    return answer


_ = input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p = list(map(int, input().split()))
print(' '.join(map(str, find_correct_study_order(a, b, p))))

examples = [
    ((
        5,
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 0, 1, 0, 0]
    ), [1, 5, 2, 4, 3]),
    ((
        6,
        [3, 10, 6, 2, 10, 1],
        [3, 5, 10, 7, 5, 9],
        [0, 0, 1, 1, 0, 1]
    ), [2, 5, 3, 6, 1, 4])
]

for inp, ans in examples:
    _, a, b, p = inp
    res = find_correct_study_order(a, b, p)
    print(inp, res, ans)
