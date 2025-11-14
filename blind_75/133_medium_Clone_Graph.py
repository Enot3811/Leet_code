"""133. Clone Graph

https://leetcode.com/problems/clone-graph/description/?envType=problem-list-v2&envId=oizxjoit

Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed).
For example, the first node with val == 1, the second node with val == 2, and so on.
The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph.
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1.
You must return the copy of the given node as a reference to the cloned graph.
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Размышления
# Проблема в этой задаче лишь в одном вопросе - что делать с петлями?
# Решение - будем складывать все созданные ноды в словарь.
# Ключём мог бы быть их хеш, но здесь нам дают их уникальные значения
# Если мы создаём соседа, а он уже был создан, то мы просто возьмём его из словаря
# В противном случае же полноценное создание новой ноды

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        self.new_nodes = {}
        return self.create_node(node)


    def create_node(self, node: 'Node'):
        # Если эта нода уже была создана
        if node.val in self.new_nodes:
            return self.new_nodes[node.val]
        
        # Создаём новую ноду
        self.new_nodes[node.val] = Node(node.val)

        # Создаём соседей для неё
        for neighbor in node.neighbors:
            self.new_nodes[node.val].neighbors.append(self.create_node(neighbor))
        return self.new_nodes[node.val]
