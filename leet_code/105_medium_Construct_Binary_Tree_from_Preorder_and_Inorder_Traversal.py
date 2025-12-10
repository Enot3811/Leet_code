"""105. Construct Binary Tree from Preorder and Inorder Traversal

Check the image and tests!
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given two integer arrays preorder and inorder where preorder is the preorder traversal
of a binary tree and inorder is the inorder traversal of the same tree,
construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""


# Размышления
# Задача имеет два подхода к своему решению. Первый укладывается в парадигму dfs.
# В preorder у нас первый элемент это корень, то есть мы можем создать ноду.
# А затем нам нужно рекурсивно создать левую и правую ноды из оставшихся элементов,
# то есть решение подзадачи с уменьшенной выборкой.
# Единственная сложность здесь это то, что мы не знаем, какая часть числе идёт в левую
# ветвь, а какая в правую, но для этого есть inoroder.
# Так как inorder идёт слева направо, то мы можем просто найти текущий элемент,
# и все числа, что были слева от него в inorder, это левая ветвь.
# Количество элементов будет одинаковым, просто в другом порядке.
# То есть мы теперь можем запустить создание веток на кусках исходных списков.


from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        mid = inorder.index(preorder[0])
        node = TreeNode(preorder[0])
        # 1-й элемент использовали сейчас, потому вырезаем его
        node.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        node.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return node

# Проблема такого исходного решения в поиске индекса на каждой итерации,
# что при худшем случае, когда дерево это одна сплошная левая ветка, выродится в n^2.
# И расход памяти огромен, так как мы всё время копируем списки при рекурсии, тоже n^2.
# Оптимизируем с помощью хешмапы, чтобы искать индекс текущего элемента за 1.
# А вместо копий списков будем передавать индексы границ.
# С границами немного сложная логика. Введём индекс для текущего элемента в preorder.
# Для взятия значений из списков будем использовать только его,
# а модифицировать будем его только через +1 на каждой итерации.
# Ведь preorder сам по себе даёт нам элементы в правильном для создания дерева порядке.
# А l и r индексы помогут нам вовремя остановиться, чтобы вернуться и переключиться
# на правую ветку.
# Такая оптимизация уже даёт n как по скорости, так и по памяти.

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}
        # Индекс текущего элемента
        self.pre_idx = 0
        def dfs(l: int, r: int) -> Optional[TreeNode]:
            # Закончились элементы для ветки
            if l > r:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            # С индексами всё та же логика, но используем их только для inorder
            mid = indices[root_val]
            # Обрезаем текущий элемент, левые налево, правые направо
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        return dfs(0, len(inorder) - 1)

# А теперь избавление от рекурсии.
# Задача сразу показалась похожей на "Kth Smallest Element in a BST (230)".
# Мы можем идти по inorder создавая ноды для левой ветки вплоть до момента,
# пока inorder[j] не станет равных preorder[0].
# То есть прямой проход до самого левого элемента как и в той задаче.
# Используем ту же логику с pre_idx. 
# Проходим по preorder, он даёт элементы в правильном порядке.
# Нужно лишь определить, правая или левая ветка.

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root]
        j = 0
        for i in range(1, len(preorder)):
            # Создаём ноду с текущим значением, но пока никуда её не определяем
            node = TreeNode(preorder[i])

            # Спускаемся влево до тех пор, пока не равны.
            if stack[-1].val != inorder[j]:
                stack[-1].left = node
                stack.append(node)
            # Если предыдущий равен inorder, то левая ветка всё
            else:
                # Теперь у нас есть два пути: стек и inorder.
                # Они будут равны до момента развилки.
                # Стек пойдёт дальше наверх, а inorder завернёт в правую ветку
                # Ищем этот момент, и туда приткнём текущую новую ноду
                while len(stack) > 0 and stack[-1].val == inorder[j]:
                    last_popped = stack.pop()
                    j += 1
                
                # last_popped последняя нода из стека, которая была равна.
                # Дальше в стеке уже путь наверх
                last_popped.right = node
                stack.append(node)
        return root
