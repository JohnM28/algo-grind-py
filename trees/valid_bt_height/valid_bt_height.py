"""
Given a binary tree, determine if it is height-balanced
    A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
"""
from trees.binary_tree import TreeNode


class Solution:

    def balanced_bt(self, root: TreeNode) -> bool:
        return self._bfs(root) != -1

    def _bfs(self, node: TreeNode) -> int:
        if not node:
            return 0
        left_h = self._bfs(node.left)
        if left_h == -1:
            return -1

        right_h = self._bfs(node.right)
        if right_h == -1:
            return -1

        if abs(left_h - right_h) > 1:
            return -1

        return max(left_h, right_h) + 1


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(sol.balanced_bt(root))  # Output: True

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)
    print(sol.balanced_bt(root))  # Output: False