n, m = [int(i) for i in input().split()]
flights = [input().split() for i in range(m)]
flights = list(map(lambda x: tuple(map(int, x)), flights))
n_town = 1
answer = []
n_flights = 0
while n_town != n:
    available_flight = list(filter(lambda x: x[0] == n_town, flights))
    available_flight = sorted(available_flight, key=lambda x: x[1])
    max_available = available_flight[-1]
    answer.append((max_available[2] + 1) % 2)
    available_flight = list(
        filter(lambda x: x[-1] != max_available[-1], available_flight))
    if len(available_flight) == 0:
        n_flights = -1
        break
    else:
        n_town = available_flight[-1][1]
        n_flights += 1
answer.extend([1] * (n - len(answer)))
print(n_flights)
print(''.join(map(str, answer)))
