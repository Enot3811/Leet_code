'''Subsets.'''


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for number in nums:
            answer.append([number])
            if len(answer) >= 2:
                last = len(answer) - 1
                for i in range(last):
                    answer.append(answer[i] + answer[last])
        answer.append([])
        return answer


sol = Solution()
print(sol.subsets([1, 2, 3, 4]))
