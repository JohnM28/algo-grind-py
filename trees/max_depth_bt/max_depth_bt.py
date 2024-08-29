"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
from typing import Optional

from trees.binary_tree import TreeNode

class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(sol.max_depth(root))  # Output: 3

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)
    print(sol.max_depth(root))  # Output: 4