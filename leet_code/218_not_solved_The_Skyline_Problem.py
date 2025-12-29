"""The Skyline Problem."""


from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Берём первый отдельно
        cur_x1, cur_x2, cur_y = buildings[-1]
        skyline = [[cur_x2, 0]]
        # Начинаем с предпоследнего
        for i in range(len(buildings) - 2, -1, -1):
            next_x1, next_x2, next_y = buildings[i]
            
            if cur_x2 > next_x2:
                point_y = cur_y
            # cur_x2 == next_x2 or cur_x2 < next_x2:
            else:
                point_y = max(cur_y, next_y)

            if cur_y > next_y:
                point_x = cur_x1
            # cur_y == next_y or cur_y < next_y
            else:
                point_x = next_x1
                
            cur_x1, cur_x2, cur_y = next_x1, next_x2, next_y
            skyline.insert(0, [point_x, point_y])
        
        if skyline[0][0] != cur_x1:
            skyline.insert(0, [cur_x1, cur_y])

        return skyline
    

sol = Solution()

examples = [
    [[2, 9, 10], [3, 7, 15], [5, 12, 12]],
    [[1, 3, 5], [2, 5, 3], [4, 6, 2]],
    [[1, 3, 3], [1, 3, 5]],
    [[1, 3, 5], [1, 3, 3]]
]
answers = [
    [[2, 10], [3, 15], [7, 12], [12, 0]],
    [[1, 5], [4, 3], [5, 2], [6, 0]],
    [[1, 5], [3, 0]],
    [[1, 5], [3, 0]]
]

for example, answer in zip(examples, answers):
    print('ans:', sol.getSkyline(example))
    print('tru:', answer, '\n')
