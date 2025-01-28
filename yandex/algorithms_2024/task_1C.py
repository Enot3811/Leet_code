"""C. Надпись на табло
Вы получили доступ к одной из камер наблюдения в особо секретной организации.
В зоне видимости камеры находится табло, с которого вы постоянно считываете
информацию. Теперь вам нужно написать программу, которая по состоянию табло
определяет, какая буква изображена на нём в данный момент. Табло представляет
из себя квадратную таблицу, разбитую на nxn клеток. Каждый диод либо включён,
либо выключен. Введём систему координат, направив ось OX вправо,
а ось OY - вверх, приняв сторону диода равной 1.

На табло могут быть изображены только следующие буквы:
- I - прямоугольник из горящих диодов.
- O - прямоугольник из горящих диодов, внутри которого есть прямоугольник из
выключенных диодов. При этом границы выключенного прямоугольника
не должны касаться внешнего.
- C - прямоугольник из горящих диодов, внутри которого есть прямоугольник из
выключенных диодов. При этом правая граница выключенного прямоугольника
находится на правой границе внешнего прямоугольника.
- L - прямоугольник из горящих диодов внутри которого есть прямоугольник из
выключенных диодов. При этом правые верхние углы выключенного прямоугольника
и внешнего прямоугольника совпадают.
- H - прямоугольник из горящих диодов, внутри которого находятся
2 прямоугольника из выключенных диодов. При этом выключенные прямоугольники
должны иметь одинаковую ширину, находиться строго один под другим, один
прямоугольник должен касаться верхней стороны, а другой прямоугольник должен
касаться нижней стороны внешнего прямоугольника.
- P - прямоугольник из горящих диодов, внутри которого находятся
2 прямоугольника из выключенных диодов. При этом правый нижний угол первого
выключенного прямоугольника должен совпадать с правым нижним углом внешнего
прямоугольника, а другой выключенный прямоугольник должен находиться строго
выше и не касаться границ других прямоугольников, также левые границы двух
выключенных прямоугольников должны совпадать.
- X - Любое другое состояние табло.

Формат ввода:
В первой строке входных данных находится одно число (1≤n≤10) — сторона табло.
В следующих n строках находятся строки длины n из символов «.» и «#» — строки
таблицы. «.» обозначает выключенный квадратный диод табло, а «#» — горящий.

Формат вывода:
Программа должна вывести единственный символ: если данная таблица подходит под
одно из описаний букв I, O, C, L, H, P, то выведите её
(все буквы — английские). Если же данная таблица не подходит ни под какие
условия, то выведите X.

Пример 1:
Ввод:
4
.##.
.##.
.##.
....

Вывод:
I

Пример 2:
Ввод:
5
#...#
.#.#.
..#..
.#.#.
#...#

Вывод:
Х
"""


def find_intervals(table, x) -> list[list[int]]:
    intervals = []
    current_interval = []
    in_interval = False
    for y in range(len(table)):
        if table[y][x] == "#":
            if not in_interval:
                in_interval = True
                current_interval.append(y)
        else:
            if in_interval:
                current_interval.append(y)
                intervals.append(current_interval)
                current_interval = []
                in_interval = False
    else:
        if in_interval:
            current_interval.append(y + 1)
            intervals.append(current_interval)
    return intervals

def table_to_letter(table):
    status = 'find_first_intervals'
    # Сканируем слева направо
    for x in range(len(table[0])):

        # Проходим по столбцу
        intervals = find_intervals(table, x)

        if status == 'find_first_intervals':
            if len(intervals) == 1:
                status = 'find_i'
                check_intervals = intervals
            elif len(intervals) > 1:
                return 'X'
        elif status == 'find_i':
            if len(intervals) == 0:
                status = 'i_end'
            elif len(intervals) == 1:
                if intervals[0] == check_intervals[0]:
                    continue
                elif intervals[0][1] == check_intervals[0][1] and intervals[0][0] > check_intervals[0][0]:
                    status = 'find_l'
                    check_intervals = intervals
                elif intervals[0][0] > check_intervals[0][0] and intervals[0][1] < check_intervals[0][1]:
                    status = 'find_h'
                    left_intervals = check_intervals
                    check_intervals = intervals
                else:
                    return 'X'
            elif len(intervals) == 2:
                if intervals[0][0] == check_intervals[0][0] and intervals[1][1] < check_intervals[0][1]:
                    status = 'find_p'
                    check_intervals = intervals
                elif intervals[0][0] == check_intervals[0][0] and intervals[1][1] == check_intervals[0][1]:
                    status = 'find_c'
                    left_intervals = check_intervals
                    check_intervals = intervals
                else:
                    return 'X'
            else:
                return 'X'
        elif status == 'find_l':
            if len(intervals) == 0:
                status = 'l_end'
            elif len(intervals) == 1:
                if intervals[0] != check_intervals[0]:
                    return 'X'
            else:
                return 'X'
        elif status == 'find_h':
            if len(intervals) == 1:
                if intervals[0] == check_intervals[0]:
                    continue
                elif left_intervals[0] == intervals[0]:
                    status = 'right_h'
                    check_intervals = intervals
                else:
                    return 'X'
            else:
                return 'X'
        elif status == 'right_h':
            if len(intervals) == 0:
                status = 'h_end'
            elif len(intervals) == 1:
                if intervals[0] != check_intervals[0]:
                    return 'X'
            else:
                return 'X'
        elif status == 'find_p':
            if len(intervals) == 2:
                if intervals != check_intervals:
                    return 'X'
            elif len(intervals) == 1:
                if intervals[0][0] == check_intervals[0][0] and intervals[0][1] == check_intervals[1][1]:
                    status = 'p_right'
                    check_intervals = intervals
                else:
                    return 'X'
            else:
                return 'X'
        elif status == 'p_right':
            if len(intervals) == 0:
                status = 'p_end'
            elif len(intervals) == 1:
                if intervals[0] != check_intervals[0]:
                    return 'X'
            else:
                return 'X'
        elif status == 'find_c':
            if len(intervals) == 0:
                status = 'c_end'
            elif len(intervals) == 2:
                if intervals != check_intervals:
                    return 'X'
            elif len(intervals) == 1:
                if intervals == left_intervals:
                    status = 'find_o'
                    check_intervals = intervals
                else:
                    return 'X'
            else:
                return 'X'
        elif status == 'find_o':
            if len(intervals) == 0:
                status = 'o_end'
            elif len(intervals) == 1:
                if intervals == check_intervals:
                    continue
                else:
                    return 'X'
            else:
                return 'X'
        elif status == 'i_end' or status == 'l_end' or status == 'h_end' or status == 'p_end' or status == 'c_end' or status == 'o_end':
            if len(intervals) != 0:
                return 'X'
    else:
        if status == 'i_end' or status == 'find_i':
            return 'I'
        elif status == 'l_end' or status == 'find_l':
            return 'L'
        elif status == 'h_end' or status == 'right_h':
            return 'H'
        elif status == 'p_end' or status == 'p_right':
            return 'P'
        elif status == 'c_end' or status == 'find_c':
            return 'C'
        elif status == 'o_end' or status == 'find_o':
            return 'O'
        else:
            return 'X'
n = int(input())
table = [input() for _ in range(n)]
print(table_to_letter(table))


tests = [
    ((8,
      '..###...',
      '.#......',
      '.#......',
      '.#......',
      '.#......',
      '.#......',
      '..###...',
      '........'), 'X'),
    # ((4,
    #   ".##.",
    #   ".##.",
    #   ".##.",
    #   "...."), "I"),
    # ((4,
    #   "....",
    #   "#...",
    #   "#...",
    #   "...."), "I"),
    # ((4,
    #   "####",
    #   "####",
    #   "####",
    #   "####"), "I"),
    # ((4,
    #   "#...",
    #   "#...",
    #   "#...",
    #   "####"), "L"),
    # ((4,
    #   "..#.",
    #   "..##",
    #   "....",
    #   "...."), "L"),
    # ((4,
    #   ".#..",
    #   ".#..",
    #   ".##.",
    #   "...."), "L"),
    # ((4,
    #   ".#..",
    #   ".##.",
    #   ".##.",
    #   "...."), "L"),
    # ((4,
    #   "#..#",
    #   "#..#",
    #   "####",
    #   "#..#"), "H"),
    # ((4,
    #   ".#.#",
    #   ".###",
    #   ".#.#",
    #   "...."), "H"),
    # ((4,
    #   ".#.#",
    #   ".###",
    #   ".###",
    #   ".#.#"), "H"),
    # ((4,
    #   ".###",
    #   ".#.#",
    #   ".###",
    #   ".#.."), "P"),
    # ((6,
    #   '.####.',
    #   '.#..#.',
    #   '.#..#.',
    #   '.####.',
    #   '.#....',
    #   '.#....'), 'P'),
    # ((6,
    #   '.#####',
    #   '.#####',
    #   '.#...#',
    #   '.#####',
    #   '.#####',
    #   '.#....'), 'P'),
    # ((6,
    #   '.####.',
    #   '.#....',
    #   '.#....',
    #   '.#....',
    #   '.#....',
    #   '.####.'), 'C'),
    # ((6,
    #   '......',
    #   '......',
    #   '......',
    #   '...###',
    #   '...#..',
    #   '...###'), 'C'),
    # ((6,
    #   '.####.',
    #   '.#..#.',
    #   '.#..#.',
    #   '.#..#.',
    #   '.#..#.',
    #   '.####.'), 'O'),
    # ((6,
    #   '......',
    #   '......',
    #   '......',
    #   '...###',
    #   '...#.#',
    #   '...###'), 'O'),
    # ((6,
    #   '......',
    #   '......',
    #   '......',
    #   '...##.',
    #   '...#..',
    #   '...###'), 'X'),
    # ((6,
    #   '##....',
    #   '#.....',
    #   '##....',
    #   '...###',
    #   '...#..',
    #   '...###'), 'X'),
    # ((6,
    #   '..##..',
    #   '......',
    #   '......',
    #   '......',
    #   '......',
    #   '..##..'), 'X'),
    # ((6,
    #   '.####.',
    #   '.#....',
    #   '.#....',
    #   '.#....',
    #   '.#....',
    #   '.#....'), 'X'),
    # ((6,
    #   '.#####',
    #   '.#....',
    #   '.#....',
    #   '.#####',
    #   '.#....',
    #   '.#....'), 'X'),
    # ((6,
    #   '.####.',
    #   '.#..#.',
    #   '.#....',
    #   '.####.',
    #   '.#....',
    #   '.#....'), 'X'),
    # ((6,
    #   '.###..',
    #   '.#..#.',
    #   '.#..#.',
    #   '.###..',
    #   '.#....',
    #   '.#....'), 'X'),
    # ((4,
    #   ".#..",
    #   ".#.#",
    #   ".###",
    #   ".#.#"), "X"),
    # ((4,
    #   "....",
    #   "....",
    #   "....",
    #   "...."), "X"),
    # ((4,
    #   "####",
    #   "#..#",
    #   "#..#",
    #   "#..#"), "X"),
    # ((4,
    #   "#..#",
    #   "#..#",
    #   "#..#",
    #   "####"), "X"),
    # ((4,
    #   ".#..",
    #   ".#..",
    #   ".##.",
    #   "...#"), "X"),
    # ((4,
    #   "#..#",
    #   "#...",
    #   "#...",
    #   "####"), "X"),
    # ((4,
    #   "##.#",
    #   "##.#",
    #   "##.#",
    #   "##.#"), "X"),
    # ((5,
    #   "#...#",
    #   ".#.#.",
    #   "..#..",
    #   ".#.#.",
    #   "#...#"), "X"),
    # ((10,
    #   '..........',
    #   '.#########',
    #   '.#########',
    #   '.#########',
    #   '........##',
    #   '........##',
    #   '.#########',
    #   '..........',
    #   '..........',
    #   '..........'), 'X'),
    # ((10,
    #   '..........',
    #   '.#########',
    #   '.#########',
    #   '.#########',
    #   '.#......##',
    #   '.#......##',
    #   '.#########',
    #   '..........',
    #   '..........',
    #   '..........'), 'O'),
    # ((1, '.'), 'X'),
    # ((1, '#'), 'I'),
    # ((10,
    #   '..........',
    #   '.#########',
    #   '.#########',
    #   '.#########',
    #   '.#......##',
    #   '.#......##',
    #   '.#########',
    #   '..........',
    #   '..........',
    #   '..........'), 'O'),
    # ((10,
    #   '..........',
    #   '.#########',
    #   '.#########',
    #   '.#########',
    #   '.#......##',
    #   '.#......##',
    #   '.#########',
    #   '.#........',
    #   '..........',
    #   '..........'), 'P'),
    # ((10,
    #   '..........',
    #   '.#########',
    #   '.#########',
    #   '.#########',
    #   '.#......##',
    #   '.#......##',
    #   '.#########',
    #   '........#.',
    #   '..........',
    #   '..........'), 'X'),
]

for inp, ans in tests:
    res = table_to_letter(inp[1:])
    print(inp[1:], res, ans)

