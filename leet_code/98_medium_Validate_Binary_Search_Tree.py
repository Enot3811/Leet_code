"""98. Validate Binary Search Tree

Check the tests!
https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less
than the node's key.
The right subtree of a node contains only nodes with keys strictly greater
than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
The number of nodes in the tree is in the range [1, 10**4].
-2**31 <= Node.val <= 2**31 - 1
"""

# Размышления
# Главная уловка задачи в том, что выполнение условия для текущей ноды не гарантирует
# выполнение условия для всего дерева.
# Если мы в какой-то ноде пошли направо, то ВСЕ дальнейшие значения должны быть больше
# той ноды. И то же самое про левую.
# Необходимо пронести эту связь через все ветвления и спуски, при этом сделать это
# эффективно, без списков и линейных проверок.
# Здесь может помочь внимательный осмотр длинного дерева.
# Когда у нас идёт долгий спуск по одной ветви, можно удобно отслеживать условие,
# в каких рамках должен удерживаться текущий узел.
# По сути у него всегда будет две границы, значения меньше/больше которых он не может
# быть.
# Эти значения будут обновляться по мере выбора правой/левой ветви, и по итогу условие
# будет становиться всё строже.


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def process_node(
            node: Optional[TreeNode],
            left_bound: Optional[int] = None,
            right_bound: Optional[int] = None
        ) -> bool:
            if node is None:
                return True
            # Если текущая нода входит в диапазон
            if ((left_bound is None or left_bound < node.val) and
                (right_bound is None or right_bound > node.val)
            ):
                # То сужаем диапазон и проверяем детей
                return (
                    # Идём влево, все меньше текущей
                    process_node(node.left, left_bound, node.val) and
                    # Идём вправо, все больше текущей
                    process_node(node.right, node.val, right_bound)
                )
                # На примере правой:
                # Правая граница не движется, а левая становится больше,
                # то есть прижимает нас к правой.
                # Правая осталась статичной с того момента, когда мы пошли влево.
            return False
        return process_node(root)
