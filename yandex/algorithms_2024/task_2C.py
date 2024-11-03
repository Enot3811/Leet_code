"""https://contest.yandex.ru/contest/66793/problems/C/"""


def monument_dist(min_dist: int, monuments: list[int]) -> int:
    left = 0
    answer = 0
    right = 0
    for right in range(len(monuments)):
        while monuments[right] - monuments[left] > min_dist:
            left += 1
            answer += len(monuments) - right
    return answer

n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(monument_dist(k, arr))

examples = [
    ((4, [1, 3, 5, 8]), 2),
    ((5, [1, 2, 8, 9]), 4),
    ((5, [1, 2, 3, 4, 5, 7]), 1),
    ((3, [1, 2]), 0),
    ((3, [1, 5]), 1),
    ((5, [1, 2, 3, 6, 7, 8, 15]), 9)
]

for inp, ans in examples:
    print(inp, monument_dist(*inp), ans)
