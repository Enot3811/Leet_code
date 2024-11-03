"""https://contest.yandex.ru/contest/66793/problems/A/"""


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
