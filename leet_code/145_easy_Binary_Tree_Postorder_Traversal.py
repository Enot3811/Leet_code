"""145. Binary Tree Postorder Traversal

Check the images and tests!
https://leetcode.com/problems/binary-tree-postorder-traversal/

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,6,7,5,2,9,8,3,1]

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]

Constraints:
The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Размышления
# Стартовая задача на изучение post order dfs.
# Идея в том, чтобы сначала обработать потомков, а потом уже делать что-то с текущим.
# Простая, но не всегда интуитивная идея.

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            ans.append(node.val)
        dfs(root)
        return ans

# Реализация без рекурсии за 2n
# Есть реализация за n без bool пометок, но она совершенно не интуитивная.
# Её только зубрить.
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        # Будем вместе с самой нодой хранить флаг, обозначающий состояние обработки.
        # False - мы ещё не обработали детей, True - обработали
        stack = [(root, False)]
        while stack:
            node, status = stack.pop()
            if node is None:
                continue
            # Это означает, что мы вернулись к этой ноде уже второй раз,
            # обработав детей
            if status:
                ans.append(node.val)
            # False же означает, что встретили ноду в первый раз
            else:
                # Кладём ноду второй раз, но уже с пометкой
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        return ans

