"""236. Lowest Common Ancestor of a Binary Tree

Check images!
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA)
of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
between two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5,
since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 10**5].
-10**9 <= Node.val <= 10**9
All Node.val are unique.
p != q
p and q will exist in the tree.
"""

# Теги
# Рекурсия (recursion), Двоичное дерево (binary tree)

# Размышления
# Есть два случая которые мы ищем:
# 1) У ноды где-то слева и справа находятся p и q
# 2) Сама нода является p или q, и у неё одна из ветвей содержит второй искомый
# Можно сделать сложный пайплайн для поиска таких условий.
# Главная проблема будет в том, чтобы отличить, когда мы просто нашли p или q от того,
# что p или q являются непосредственно ответом.
# Но если привязаться к условию, что p и q обязательно существуют,
# то можно сделать проще.
# Если мы ловим и p и q, то как и раньше эта нода будет ответом.
# Но теперь если мы ловим один из p или q, то просто не заморачиваемся и передаём его.
# В итоге может сложиться ситуация, что в корень придёт лишь одна нода.
# И она же и будет ответом. Ведь другую мы не видим, но знаем, что она есть.
# Значит он спрятана под вернувшейся.
# Это будет немного затратнее, потому как нам придётся обходить остаток дерева,
# даже если мы уже нашли две ноды.
# Но зато очень коротко и лаконично.
# Чтобы улучшить производительность, самой простой идеей будет использование переменной
# объекта.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        if root is None:
            return None
        if root == q or root == p:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        elif left:
            return left
        else:
            return right
