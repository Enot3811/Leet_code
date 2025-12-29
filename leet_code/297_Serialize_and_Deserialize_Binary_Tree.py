"""297. Serialize and Deserialize Binary Tree.

https://leetcode.com/problems/serialize-and-deserialize-binary-tree

Serialization is the process of converting a data structure
or object into a sequence of bits so that it can be stored in a file
or memory buffer, or transmitted across a network connection link
to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization
algorithm should work. You just need to ensure that a binary tree
can be serialized to a string and this string can be deserialized
to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes
a binary tree. You do not necessarily need to follow this format,
so please be creative and come up with different approaches yourself.
"""


from typing import Optional
from collections import deque


class TreeNode:

    def __init__(
        self,
        value: int
    ):
        self.val: int = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

# Размышления
# Будем проходить по дереву. Сначала левая нода, потом правая.
# И в таком же порядке просто выписывать значения в список
# В итоге в списке будут значения ровно в том же порядке, что и мы проходились по 
# древу. Где нет значений пишем что-то служебное, вроде null.
# При десериализации проходим по дереву "построчно", кладя на каждых двух элементах
# ноду в стек.

class Codec:
    def serialize(self, root: TreeNode) -> str:
        available_nodes = deque([root])
        val_list = []
        while len(available_nodes) != 0:
            current_node = available_nodes.popleft()
            if current_node is None:
                val_list.append('null')
            else:
                val_list.append(str(current_node.val))
                available_nodes.append(current_node.left)
                available_nodes.append(current_node.right)
        return ' '.join(val_list)

    def deserialize(self, data: str) -> TreeNode:
        if data == '' or data == 'null':
            return None
        nodes = data.split()
        val = int(nodes.pop(0))
        root = TreeNode(val)
        available_nodes = deque([root])
        current_node = None

        for i, val in enumerate(nodes):
            if val != 'null':
                new_node = TreeNode(int(val))
                available_nodes.append(new_node)
            else:
                new_node = None
            if i % 2 == 0:
                current_node = available_nodes.popleft()
                current_node.left = new_node
            else:
                current_node.right = new_node
        return root


sol = Codec()
tree_str = '1 2 3 null 4 5 6 7 null null 8'
#           1
#      /         \
#     2           3
#   /   \       /   \
#  n     4     5     6
# / \   / \   / \   / \
#7   n n   8 n   n n   n
tree = sol.deserialize(tree_str)
print(sol.serialize(tree))
