"""https://contest.yandex.ru/contest/66793/problems/D/"""


def task_list(diff: int, tasks: list[int]) -> int:
    tasks.sort()
    n_days = 0
    left = 0
    right = 0
    while right < len(tasks):
        if tasks[right] - tasks[left] <= diff:
            right += 1
            n_days = max(n_days, right - left)
        else:
            left += 1
    return n_days

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(task_list(k, arr))

examples = [
    (1, [1,1,1,1,1,1], 6),
    (2, [3, 8, 5, 7, 1, 2, 4, 9, 6], 3),
    (2, [3, 8, 5, 7, 1, 2, 4, 9, 8, 8, 8, 8, 8, 6], 8),
    (2, [4, 2, 1], 2),
    (1, [32, 77, 1, 100], 1),
    (1, [1, 3, 1], 2),
    (0, [1, 3, 1], 2),
    (3, [1, 4, 7, 15, 20, 100, 119, 121], 2)
]

for diff, tasks, ans in examples:
    # tasks.sort()
    # tasks = deque(tasks)
    print(diff, tasks, task_list(diff, tasks), ans)

# with open(r'C:\Users\enot\Downloads\Telegram Desktop\21') as f:
#     text = f.readlines()
# n, k = map(int, text[0].split())
# arr = list(map(int, text[1].split()))

# print(task_list(k, arr))

