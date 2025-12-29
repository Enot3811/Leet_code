"""104. Maximum Depth of Binary Tree

Check the image and tests!
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
The number of nodes in the tree is in the range [0, 10**4].
-100 <= Node.val <= 100
"""

# Размышления
# Чтобы найти самую глубокую ветку так или иначе придётся пройти по всему дереву.
# Если делать рекурсивно, то текущая нода +1 и плюс то, что вернут ветки.
# В итоге наверх выйдет максимальное значение глубины.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Но при желании можно обойти и без рекурсии, хотя и надо придумать, как в таком случае
# отслеживать глубину нод, извлекаемых из стека.
# Здесь можно вспомнить задачу "Binary Tree Level Order Traversal" (102),
# где было необходимо пройти по дереву по уровням.
# Применив эту идею здесь, мы можем вернуть номер последнего уровня.

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return []
        level_counter = 0
        nodes = deque([root])
        while len(nodes) != 0:
            # В стеке в данный момент только ноды текущего уровня
            for _ in range(len(nodes)):
                node = nodes.popleft()
                if node.left is not None:
                    nodes.append(node.left)
                if node.right is not None:
                    nodes.append(node.right)
            level_counter += 1
        return level_counter
