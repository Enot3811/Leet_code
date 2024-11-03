"""https://contest.yandex.ru/contest/66793/problems/B/"""


def car_sum(arr: list[int], k: int) -> int:
    left = 0
    cur_sum = 0
    answer = 0
    for right in range(len(arr)):
        cur_sum += arr[right]
        while cur_sum > k:
            cur_sum -= arr[left]
            left += 1
        if cur_sum == k:
            answer += 1
    return answer

n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(car_sum(arr, k))

examples = [
    (17, [7, 10, 7, 10], 3),
    (10, [1, 2, 3, 4, 1], 2),
    (17, [17, 7, 10, 7, 10], 4)
]

for k, arr, expected in examples:
    print(arr, k, car_sum(arr, k), expected)
