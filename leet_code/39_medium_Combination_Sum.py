"""39. Combination Sum

https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates
where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers
is different.

The test cases are generated such that the number of unique combinations
that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""

# Размышления
# Крайне не интуитивное оптимальное решение.
# Сперва в голову приходит поиск в глубину, но тогда будут появляться дубли
# Так как чисел в задаче не очень много, то можно было бы наивно решить, используя
# сет и сортировку, чтобы отбрасывать дубли.
# Оптимальное решение подсмотрел у neetcode https://www.youtube.com/watch?v=GBKI9VSKdGg
# Введём индекс, отрезающий кандидатов, которых мы бы не хотели далее использовать
# А далее представим задачу как дерево с двумя выборами
# 1) Мы прибавляем текущего кандидата (на котором индекс), и ничего не делаем с индексом
# (все кандидаты так же доступны)
# 2) Мы не прибавляем никого, но сдвигаем индекс вперёд, не давая далее использовать
# текущего кандидата
# Получается вот такой не самый интуитивный перебор,
# но покрывающий все случаи без дублей
#                              /                                           \
#                            [1]                                           []
#                   /                      \                       /               \
#               [1,1]                       [1]                  [2]               []
#             /          \                 /    \              /       \          /   \
#      [1,1,1]           [1,1]         [1,2]    [1]       [2,2]         [2]     [3]   []
#      /     \           /   \         /   \    /  \     /    \         / \      /  \ /\
# [1,1,1,1] [1,1,1] [1,1,2] [1,1] [1,2,2] [1,2] [1,3] [2,2,2] [2,2] [2,3] [2] [3,3]...
# Левая ветка отвечает за количество повторов текущего кандидата,
# а правая за переход на следующих кандидатов



from typing import List

class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def step(cand_idx: int, curr_sum: int, curr_list: List[int]):
            if curr_sum == target:
                result.append(curr_list.copy())
                return
            # Если исчерпали всех кандидатов или переступили таргет
            elif cand_idx >= len(candidates) or curr_sum > target:
                return
            else:
                curr_list.append(candidates[cand_idx])
                step(cand_idx, curr_sum + candidates[cand_idx], curr_list)
                curr_list.pop()
                step(cand_idx + 1, curr_sum, curr_list)
        
        step(0, 0, [])
        return result
