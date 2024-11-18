"""486. Predict the Winner

https://leetcode.com/problems/predict-the-winner/description/
"""


from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        game_sum = self.make_step(nums, step=1, left=0, right=len(nums) - 1)
        return game_sum >= 0

    def make_step(
        self, nums: List[int], step: int, left: int, right: int
    ) -> int:
        if left > right:
            return 0

        # Первый игрок
        if step % 2 == 1:
            # Прибавляет
            var1 = self.make_step(nums, step + 1, left + 1, right) + nums[left]
            var2 = self.make_step(nums, step + 1, left, right - 1) + nums[right]
            # Максимизирует сумму
            result = max(var1, var2)

        # Второй игрок
        else:
            # Отнимает
            var1 = self.make_step(nums, step + 1, left + 1, right) - nums[left]
            var2 = self.make_step(nums, step + 1, left, right - 1) - nums[right]
            # Минимизирует сумму
            result = min(var1, var2)
        return result
    

def rand_list(l: int, min_v: int = 0, max_v: int = 100) -> List[int]:
    from random import randint
    return [randint(min_v, max_v) for _ in range(l)]


if __name__ == "__main__":
    examples = [
        ([1, 5, 2], False),
        ([1, 5, 233, 7], True),
        ([0], True),
        ([0, 1], True),
        ([0, 1, 0], False),
        ([1, 255, 233, 7], True),
    ]

    sol = Solution()
    for nums, expected in examples:
        res = sol.predictTheWinner(nums)
        print(nums, res, expected)
