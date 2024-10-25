from sklearn.linear_model import LinearRegression

with open('input.txt') as f:
    lines = f.readlines()

m, s = tuple(map(int, lines[0].split()))
n = int(lines[1])
history = map(lambda line: line.split(), lines[2:2 + n])
history = [list(map(int, line)) for line in history]
history = [(tuple(line[:3]), tuple(line[3:])) for line in history]
history = sorted(history, key=lambda line: line[0])

q = int(lines[2 + n])
new_lines = map(lambda line: line.split(), lines[3 + n:])
new_lines = [list(map(int, line)) for line in new_lines]
new_history = list(filter(lambda line: line[0] == 1, new_lines))
to_preds = list(filter(lambda line: line[0] == 2, new_lines))
new_history = list(map(lambda line: line[1:], new_history))
to_preds = list(map(lambda line: line[1:], to_preds))

# print(new_history)
# print(to_preds)

days = [[] for _ in range(7)]
for line in history:
    day = line[0][1]
    hour = line[0][2]
    orders = line[1]
    days[day].append((hour, orders))

# print(days)

regressions = []
for i, day in enumerate(days):
    x = []
    y = [[] for _ in range(m)]
    for day_orders in day:
        x.append([day_orders[0]])
        for j, order in enumerate(day_orders[1]):
            y[j].append(order)
    day_regressions = []
    # print(y)
    for j in range(m):
        if len(x) == 0:
            reg = day_regressions[j - 1]
            day_regressions.append(reg)
        else:    
            day_regressions.append(LinearRegression().fit(x, y[j]))
    regressions.append(day_regressions)

# print(regressions)
# regressions[1][0].predict([10])

for to_pred in to_preds:
    day = to_pred[1]
    hour = to_pred[2]
    preds = []
    for i in range(m):
        preds.append(regressions[day][i].predict([[hour]])[0])
    # print(preds)
    
    n_courier = s
    i = 0
    while n_courier != 0:
        if preds[i] > 0:
            preds[i] -= 1
            n_courier -= 1
        i = (i + 1) % m
    print(*preds)
