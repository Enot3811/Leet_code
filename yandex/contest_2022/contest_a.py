# n = 10
# # 1 3 6 9 10
# # 2 4 8 9 10
# # 5 7 1
# nps = [3, 4, 6, 8, 7, 9, 1, 9, 10, -1]
n = int(input())
nps = list(map(lambda x: max(int(x) - 1, -1), input().split()))
memory = set()
answer = True

for current, nxt in enumerate(nps):
    path = set()
    while current != -1:
        if current in memory:
            break
        elif current in path:
            answer = False
            break
        else:
            path.add(current)
        current = nxt
        nxt = nps[nxt]
    else:
        memory |= path

    if not answer:
        break

print('Yes' if answer else 'No')
