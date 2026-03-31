"""101. Symmetric Tree

Check the images!
https://leetcode.com/problems/symmetric-tree/

Given the root of a binary tree,
check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 
Follow up: Could you solve it both recursively and iteratively?
"""

# Теги
# Двоичное дерево (binary tree), Очередь (queue)

# Размышления
# Идея здесь ясна, что нужен обход в ширину с очередью,
# который позволит проверять дерево построчно.
# Но главное здесь не улететь сразу реализовывать это прямо в лоб.
# Это можно сделать, но получится слишком переусложнённо.
# Вместо поэлементного построчного подхода возьмём ноды парами.
# У пары нод должны быть равны значения, а затем:
# Левый лист левой равен правому листу правой,
# Правый лист левой равен левому листу правой.
# И как раз и добавим их вот такими парами для последующей проверки:
# (node1.left, node2.right), (node1.right, node2.left)
# То есть подойти к решению рекурсивно.

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root.left, root.right)])

        while queue:
            node1, node2 = queue.popleft()

            if not node1 and not node2:
                continue

            # Один из них пустой, либо не равны
            if not node1 or not node2 or node1.val != node2.val:
                return False

            queue.append((node1.left, node2.right))
            queue.append((node1.right, node2.left))
        
        return True
