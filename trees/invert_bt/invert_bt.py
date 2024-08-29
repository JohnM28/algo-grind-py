"""
Given the root of a binary tree, invert the tree, and return its root.
"""
from trees.binary_tree import TreeNode
from typing import Optional


class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts the binary tree
        :param root:
        :return:
        """
        def bfs(root : TreeNode) -> None:
            """
            Perform a breadth-first traversal of the tree.
            :param root:
            :return:
            """
            if not root:
                return
            root.left, root.right = root.right, root.left
            bfs(root.left)
            bfs(root.right)

        bfs(root)
        return root
