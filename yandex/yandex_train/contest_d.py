"""Коллекция статуэток."""


from random import randint
from time import time


def find_cheaper_cost(k, statuettes):
    current_statuettes = []
    need_statuettes = {i: 0 for i in range(1, k + 1)}

    cheapest = float('inf')
    last_statuette = -1
    needed_count = k

    for i, statuette in enumerate(statuettes):

        if statuette <= k:
            if last_statuette == statuette:
                current_statuettes[-1] = i
            elif (len(current_statuettes) != 0 and
                    statuette == statuettes[current_statuettes[0]]):
                last_statuette = statuette
                current_statuettes.pop(0)
                current_statuettes.append(i)
            else:
                last_statuette = statuette
                current_statuettes.append(i)
                if need_statuettes[statuette] == 0:
                    needed_count -= 1
                need_statuettes[statuette] += 1

                if needed_count == 0:
                    current_cost = sum(statuettes[
                        current_statuettes[0]:current_statuettes[-1] + 1])
                    if cheapest > current_cost:
                        cheapest = current_cost

                    while len(current_statuettes) > 0:
                        idx = current_statuettes.pop(0)
                        statuette = statuettes[idx]
                        need_statuettes[statuette] -= 1

                        if need_statuettes[statuette] == 0:
                            needed_count += 1
                            break
                        elif k > 1:
                            diff = sum(statuettes[
                                idx:current_statuettes[0]
                            ])
                            current_cost -= diff

                            if cheapest > current_cost:
                                cheapest = current_cost
    # print(cheapest)
    return cheapest


if __name__ == '__main__':
    # n, k = tuple(map(int, input().split()))
    # statuettes = list(map(int, input().split()))

    # 1 2 3 2 1 3 2 1 3 2 1 4

    tests = [
        (3, [1, 2, 2, 3, 3, 1], 8),
        (3, [1, 2, 5, 4, 3], 15),
        (3, [1, 2, 6, 3, 3, 1], 12),
        (1, [6, 2, 3, 1, 2, 3], 1),
        (7, [1, 2, 3, 4, 6, 5, 7], 28),
        (2, [1, 9, 2, 4, 3, 1, 8, 2, 10, 9], 10),
        (2, [1, 1, 1, 1, 2], 3),
        (3, [1, 4, 3, 2, 2, 2, 2, 1, 3, 2, 5, 1, 3], 6),
        (3, [1, 4, 2, 1, 2, 2, 2, 2, 2, 3], 14),
        (3, [1, 4, 2, 3, 3, 3, 3, 3, 3, 3, 1], 10),
        (4, [1, 2, 3, 2, 5, 1, 2, 3, 4, 3, 2, 3, 1, 2, 3], 10)
    ]
    
    tests.append((5000000, [randint(1, 5000000) for _ in range(500000)],
                  'unknown'))

    t = time()
    for k, statuettes, answer in tests:
        print('Ans:', find_cheaper_cost(k, statuettes), 'Tru:', answer)
    print('Time:', time() - t)
