with open('input_b.txt', 'r') as f:
    data = list(map(int, f.readline().split()))

n = data[0]
buildings = data[1:]

max_building = max(buildings)

current_highest = 0
zip_line = []
for i, building in enumerate(buildings):

    if building > current_highest:
        current_highest = building
        zip_line.append(i)

    if building == max_building:
        break

current_highest = 0
zip_line_right = []
for j in range(len(buildings) - 1, -1, -1):
    if buildings[j] == max_building:
        break

    if buildings[j] > current_highest:
        current_highest = buildings[j]
        zip_line_right.insert(0, j)

zip_line += zip_line_right
max_height = 0
for i in range(len(zip_line) - 1):
    sector = buildings[zip_line[i] + 1:zip_line[i + 1]]
    if len(sector) == 0:
        continue
    height = (min(buildings[zip_line[i]], buildings[zip_line[i + 1]]) -
              min(sector))
    if height > max_height:
        max_height = height
print(max_height)
