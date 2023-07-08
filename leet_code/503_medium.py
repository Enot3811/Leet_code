"""503. Next Greater Element II."""


from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        answer = [-1 for _ in range(len(nums))]
        for n in range(2):
            for i in range(len(nums) - 1, -1, -1):
                k = len(stack) - 1
                while len(stack) > 0:
                    if nums[stack[k]] > nums[i]:
                        answer[i] = nums[stack[k]]
                        break
                    else:
                        stack.pop()
                        k -= 1
                stack.append(i)
        return answer


sol = Solution()
example = [4, 8, 2, 5, 7, 1, 6]
res = sol.nextGreaterElements(example)
print(res)
