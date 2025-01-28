"""Чтобы набрать форму к лету, Виктория решила бегать каждый день. До лета осталось всего n дней — именно на протяжении этого срока она и будет бегать. Ее личный тренер уже составил ей расписание: в -й день Виктория должна пробежать a_i километров.
Виктория считает i-й (3<=i<=n) день хорошим, если в этот день она пробежит не меньше, чем в первый день, и не больше, чем во второй день. Расписание же ей понравится, если хотя бы m дней будут хорошими. В расписании можно делать корректировки: произвольное a_i (1<=i<=n) можно увеличить или уменьшить на 1 километр. Разрешается корректировать один и тот же день несколько раз.
Какое минимальное корректировок необходимо внести в расписание, чтобы оно понравилось Виктории?

Формат входных данных:
Первая строка содержит числа n (3<=n<=2 * 10^5) и m (1<=m<=n-2) — количество дней до лета и количество хороших дней, которое необходимо Виктории, чтобы ей понравилось расписание.
Следующая строка содержит числа a_1, a_2, a_3, ..., a_n (1<=a_i<=10^9) — количество километров, которое должна пробежать Виктория согласно начальному расписанию.

Формат выходных данных:
Выведите одно число — минимальное количество корректировок, которое необходимо внести в расписание, чтобы оно понравилось Виктории.

Пример данных:
Ввод
3 1
3 4 6

Вывод
2

Комментарий к примеру:
В примере можно дважды уменьшить a_3 на единицу, чтобы расписание понравилось Виктории."""


from collections import Counter


def calculate_good_days(counter, keys, left, right):
    good_days = 0
    for key in keys:
        if left <= key <= right:
            good_days += counter[key]
    return good_days


def solve(n, m, a):
    left = a[0]
    right = a[1]

    counter = Counter(a[2:])
    keys = sorted(set(a))
    left_idx = keys.index(left)
    right_idx = keys.index(right)

    good_days = calculate_good_days(counter, keys, left, right)
    operations = 0

    while good_days < m:
        if good_days >= m:
            return operations
        
        # Куда и насколько идти
        if left_idx > 0:
            left_oper = keys[left_idx] - keys[left_idx - 1]
        else:
            left_oper = float('inf')
        if right_idx < len(keys) - 1:
            right_oper = keys[right_idx + 1] - keys[right_idx]
        else:
            right_oper = float('inf')

        if left_oper < right_oper:
            left_idx -= 1
            operations += left_oper
            left = keys[left_idx]
            good_days += counter[left]
        else:
            right_idx += 1
            operations += right_oper
            right = keys[right_idx]
            good_days += counter[right]
    return operations


# Чтение входных данных
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))


# n, m = 6, 3
# a = [8, 9, 6, 7, 15, 15, 15]
