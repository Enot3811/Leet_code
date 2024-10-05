"""Найти вертикальную ось симметрии для точек"""

from typing import List, Tuple, Optional


def find_vsim(dots: List[Tuple[int, int]]) -> Optional[float]:
    # Сортируем по y, x
    dots = sorted(dots, key=lambda x: x[::-1])
    # Проходим по точка, но анализируем каждую y ось отдельно
    current_symmetry = None
    current_y = None
    current_axis_x = []
    for dot in dots:
        if current_y is None:
            current_y = dot[1]
        else:
            # Если текущая ось закончилась
            if dot[1] != current_y:
                # Проверяем её точки на соответствие текущей симметрии
                left = 0
                right = len(current_axis_x) - 1
                while left < right:
                    sym = (current_axis_x[left] + current_axis_x[right]) / 2
                    if current_symmetry is None:
                        current_symmetry = sym
                    elif current_symmetry != sym:
                        return None
                    left += 1
                    right -= 1

                # Обновляем ось
                current_axis_x.clear()
                current_y = dot[1]
            
        current_axis_x.append(dot[0])

    # Проверяем последнюю ось
    left = 0
    right = len(current_axis_x) - 1
    while left < right:
        sym = (current_axis_x[left] + current_axis_x[right]) / 2
        if current_symmetry is None:
            current_symmetry = sym
        elif current_symmetry != sym:
            return None
        left += 1
        right -= 1

    return current_symmetry


examples = [
    ([(0, 4), (2, 4), (5, 4), (-3, 4), (1, 1), (1, 1), (3, 0), (-1, 0)], 1.0),

]

for inp, ans in examples:
    out = find_vsim(inp)
    print(inp, out, ans)
