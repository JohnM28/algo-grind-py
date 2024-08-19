"""
Problem: Given a binary tree, determine if it is a valid binary search tree (BST).
"""

from trees.binary_tree import TreeNode


class Solution:
    def is_valid_BST(self, root: TreeNode | None) -> bool:
        if not root:
            return False
        return self._traverse_and_find(root, float('-inf'), float('inf'))

    def _traverse_and_find(self, node, min_val, max_val):
        if not node:
            return True
        if not min_val < node.val < max_val:
            return False
        return (self._traverse_and_find(node.left, min_val, node.val) and
                self._traverse_and_find(node.right, node.val, max_val))

    def sol2(self, root: TreeNode | None) -> bool:
        output = []
        self.in_order_traverse(root, output)
        for i in range(len(output) - 1):
            if output[i] >= output[i + 1]:
                return False
        return True

    def in_order_traverse(self, node: TreeNode | None, output: list) -> None:
        if not node:
            return
        self.in_order_traverse(node.left, output)
        output.append(node.val)
        self.in_order_traverse(node.right, output)


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(sol.is_valid_BST(root))  # Output: True

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    print(sol.is_valid_BST(root))  # Output: False

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(6)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)
    print(sol.is_valid_BST(root))  # Output: False
