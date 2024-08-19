"""
Diameter of Binary Tree
"""
from typing import Optional
from trees.binary_tree import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> tuple:
        if not root:
            return 0, 0
        _, diameter = self._traverse_and_find(root, 0)
        return diameter

    def _traverse_and_find(self, node: TreeNode, diameter: int) -> tuple:
        if not node:
            return 0, diameter
        left, diameter = self._traverse_and_find(node.left, diameter)
        right, diameter = self._traverse_and_find(node.right, diameter)
        diameter = max(diameter, left + right)
        return 1 + max(left, right), diameter

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(sol.diameterOfBinaryTree(root))  # Output: 3

    root = TreeNode(1)
    root.left = TreeNode(2)
    print(sol.diameterOfBinaryTree(root))  # Output: 1