"""486. Predict the Winner

You are given an integer array nums.
Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first.
Both players start the game with a score of 0.
At each turn, the player takes one of the numbers from either end of the array
(i.e., nums[0] or nums[nums.length - 1])
which reduces the size of the array by 1.
The player adds the chosen number to their score.
The game ends when there are no more elements in the array.

Return true if Player 1 can win the game.
If the scores of both players are equal, then player 1 is still the winner,
and you should also return true.
You may assume that both players are playing optimally.

Example 1:
Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2.
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5.
If player 2 chooses 5, then player 1 will be left with 1 (or 2).
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
Hence, player 1 will never be the winner and you need to return false.

Example 2:
Input: nums = [1,5,233,7]
Output: true
Explanation: Player 1 first chooses 1. Then player 2 has to choose
between 5 and 7.
No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12),
so you need to return True representing player1 can win.

Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 10^7
"""


from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        self.memory = {}
        game_sum = self.make_step(nums, left=0, right=len(nums) - 1)
        return game_sum >= 0

    def make_step(
        self, nums: List[int], left: int, right: int
    ) -> int:
        # Если список закончился
        if left > right:
            return 0

        # Первый игрок
        if (len(nums) - (right - left)) % 2 == 1:
            
            # Если этот ход уже был посчитан
            if (left, right) in self.memory:
                return self.memory[(left, right)]

            # Прибавляет
            var1 = self.make_step(nums, left + 1, right) + nums[left]
            var2 = self.make_step(nums, left, right - 1) + nums[right]
            # Максимизирует сумму
            result = max(var1, var2)
            # Записывает результат
            self.memory[(left, right)] = result

        # Второй игрок
        else:
            # Если этот ход уже был посчитан
            if (left, right) in self.memory:
                return self.memory[(left, right)]

            # Отнимает
            var1 = self.make_step(nums, left + 1, right) - nums[left]
            var2 = self.make_step(nums, left, right - 1) - nums[right]
            # Минимизирует сумму
            result = min(var1, var2)
            # Записывает результат
            self.memory[(left, right)] = result

        return result


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
