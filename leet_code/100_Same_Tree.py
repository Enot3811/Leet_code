"""100. Same Tree

Check the images!
https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q,
write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
-10**4 <= Node.val <= 10**4
"""

# Теги
# Двоичное дерево (binary tree)

# Размышления
# Проходим по дереву с помощью рекурсии. Все ноды должны быть равны

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Если обоих нет
        if p is None and q is None:
            return True
        # Если одного нет или не равны
        elif p is None or q is None or p.val != q.val:
            return False
        # Если текущие ноды равны, запустить эту же задачу на два поддерева
        else:
            # Оба должны быть равны
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
