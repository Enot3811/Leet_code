'''Serialize and Deserialize Binary Tree.'''


from typing import Optional


class TreeNode:

    def __init__(
        self,
        value: int
    ):
        self.val: int = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        available_nodes = [root]
        val_list = []
        while len(available_nodes) != 0:
            current_node = available_nodes.pop(0)
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
        available_nodes = [root]
        current_node = None

        for i, val in enumerate(nodes):
            if val != 'null':
                new_node = TreeNode(int(val))
                available_nodes.append(new_node)
            else:
                new_node = None
            if i % 2 == 0:
                current_node = available_nodes.pop(0)
                current_node.left = new_node
            else:
                current_node.right = new_node
        return root


sol = Codec()
tree_str = ''
tree = sol.deserialize(tree_str)
print(sol.serialize(tree))
