"""230. Kth Smallest Element in a BST

Check the images and tests!
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given the root of a binary search tree, and an integer k,
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 10**4
0 <= Node.val <= 10**4

Follow up: If the BST is modified often (i.e., we can do insert and delete operations)
and you need to find the kth smallest frequently, how would you optimize?
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Размышления
# В задаче несколько идей, до которых надо дойти.
# 1) Как вообще искать k-й от минимума?
# В бинарном дереве если мы хотим найти минимум, мы всегда идём влево.
# По итогу мы можем быстро прийти к минимуму и начать считать k уже от него.
# Но как это делать? Если при возврате из левой ветки можно просто делать +1,
# то с правой сложнее.
# Проход должен быть слева направо через текущий узел.
# И здесь возникает второй момент
# 2) Как лаконично сделать счёт в разных ветвях?
# Слева хочется делать +1 при подъёме, а справа +1 при спуске.
# Но на самом деле можно сделать иную формулировку:
# Мы будем делать +1 при возврате из левой ветки, а потом пойдём в правую.
# То есть никакого +1 при спуске.
# При входе в правую ветвь мы не считаем её, а пытаемся сразу уйти в её левую,
# так как она меньше, и только при возврате мы сделаем +1 для текущего узла.
# Своего рода дроблённая итерация, что весьма необычно.

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        def process_node(node: Optional[TreeNode]) -> Optional[int]:
            nonlocal counter

            if node is None:
                return

            # Сразу идём влево, не обрабатывая текущую
            val = process_node(node.left)
            if val is not None:
                return val

            # После возврата учитываем текущую
            counter += 1
            if counter == k:
                return node.val

            # И если не хватило, то идём вправо
            val = process_node(node.right)
            if val is not None:
                return val

        return process_node(root)

# Если хотим избавиться от рекурсии и нелаконичных опциональных выводов,
# то есть иная интересная реализация.
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr_node = root
        counter = 0
        while len(stack) != 0 or curr_node is not None:
            # Идём налево, пока можем
            while curr_node is not None:
                stack.append(curr_node)
                curr_node = curr_node.left
            
            # Когда достаём, всё равно что возврат из левой ветки
            curr_node = stack.pop()
            counter += 1
            if counter == k:
                return curr_node.val
            
            # Пробуем идти вправо
            curr_node = curr_node.right
        
    # При этом из интересного
    # 1) Проход влево очень ловко заменяется на текущую ноду
    # 2) Очень лаконичный переход в правую ветвь
    # 3) right может быть None, и тогда просто идём следующий stack.pop без спуска влево
        