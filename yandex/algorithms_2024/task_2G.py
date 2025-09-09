"""G. Цензурное произведение

Есть строка из букв.
Мы можем вычёркивать из неё буквы, чтобы получить "ab" разными способами.

Необходимо найти длину наибольшей подстроки,
которая содержит не более C способов получить "ab".

Например, строка aabcbb сама по себе содержит 6 способов.
Если C = 4, то варианты aabc или abcb максимальное, что мы можем сделать.
"""


def find_longest_substr(s: str, c: int) -> int:
    left = 0
    right = 0
    max_len = 0
    cur_c = 0
    num_a = 0
    num_b = 0
    for right in range(len(s)):
        if s[right] == 'a':
            num_a += 1

        # Количество способов увеличивается на количество а при нахождении b
        elif s[right] == 'b':
            cur_c += num_a
            num_b += 1
    
            # И в этот момент лучше всего проверять условие
            while cur_c > c and left < right:
                
                # При удалении каждого а, количество способов уменьшается
                # на количество b, с которыми она взаимодействовала
                if s[left] == 'a':
                    num_a -= 1
                    cur_c -= num_b

                # При удалении b ничего не меняется, так как мы уже удалили все a,
                # что были перед ней (с которыми она взаимодействовала)
                elif s[left] == 'b':
                    num_b -= 1

                left += 1
        
        max_len = max(max_len, right - left + 1)

    max_len = max(max_len, right - left)

    return max_len

_, c = tuple(map(int, input().split()))
s = input()
print(find_longest_substr(s, c))


# examples = [
#     ((6, 2, "aabcbb"), 4),
#     ((6, 0, "cbcbcb"), 6),
#     ((6, 0, "abaaab"), 4)
# ]

# for inp, ans in examples:
#     _, c, s = inp
#     res = find_longest_substr(s, c)
#     print(inp, res, ans)
