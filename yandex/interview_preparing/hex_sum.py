"""Сложение шестнадцатеричных чисел"""

def hex_sum(num1: str, num2: str):

    answer = []
    add_next = 0
    for i in range(1, max(len(num1), len(num2)) + 1):
        idx1 = len(num1) - i
        idx2 = len(num2) - i
        if idx1 < 0:
            int1 = 0
        else:
            int1 = int(num1[idx1], 16)
        if idx2 < 0:
            int2 = 0
        else:
            int2 = int(num2[idx2], 16)
        digit_sum = int1 + int2 + add_next
        add_next = digit_sum // 16
        answer.insert(0, hex(digit_sum % 16)[2:])
    else:
        if add_next > 0:
            answer.insert(0, hex(add_next)[2:])

    answer = ''.join(answer)
    return answer


examples = [
    (['f', '1'], '10'),
    (['fff', '1'], '1000'),
    (['54', '3'], '57'),
    (['0', '0'], '0'),
    (['abe', 'fabe'], '1057c'),
    (['ff', 'ff'], '1fe')
]

for inp, ans in examples:
    out = hex_sum(*inp)
    print(inp, out, ans)
