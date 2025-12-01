"""124. Binary Tree Maximum Path Sum

Check the images and tests!
https://leetcode.com/problems/binary-tree-maximum-path-sum/

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes
in the sequence has an edge connecting them.
A node can only appear in the sequence at most once.
Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:
The number of nodes in the tree is in the range [1, 3 * 10**4].
-1000 <= Node.val <= 1000
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = None

        def process_node(node: Optional[TreeNode]) -> int:
            nonlocal max_path
            if not node:
                return 0
            # Если ветвь отрицательная, то в ней нет смысла
            left = max(0, process_node(node.left))
            right = max(0, process_node(node.right))
            # Если воспринимать текущую ветку как корень
            # то можно взять обе ветки
            root_val = node.val + left + right
            if max_path is None or root_val > max_path:
                max_path = root_val
            # Но если воспринимать как ветвь, то мы не можем взять обе ветки
            branch_val = node.val + max(right, left)
            return branch_val

        process_node(root)
        return max_path
