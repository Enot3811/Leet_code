"""572. Subtree of Another Tree

Check the images!
https://leetcode.com/problems/subtree-of-another-tree/

Given the roots of two binary trees root and subRoot, return true if there is a subtree
of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree
and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-10**4 <= root.val <= 10**4
-10**4 <= subRoot.val <= 10**4
"""

# Размышления
# Нет каких-то особенных подходов эффективно решить задачу.
# Просто решаем задачу №100 Same Tree для каждой ноды дерева до тех пор,
# пока не найдётся совпадение, или пока не пересечём всё дерево

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        elif self.isSameTree(root, subRoot):
            return True
        else:
            return (
                self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot)
            )
    
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
