"""
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
"""

from collections import deque
from typing import Optional, List

from trees.binary_tree import TreeNode


class Solution:
    def right_side_view(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the right side view of the binary tree Time complexity: O(n) and Space complexity: O(n)
        :param root:
        :return:
        """
        if not root:
            return []
        queue = deque([(root, 0)])
        levels = {}
        while queue:
            node, level = queue.popleft()
            levels[level] = node.val
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return list(levels.values())


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    print(sol.right_side_view(root))  # Output: [1, 3, 4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    print(sol.right_side_view(root))  # Output: [1, 3, 4, 7]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    print(sol.right_side_view(root))  # Output: [1, 3, 4, 7]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)
    root.right = TreeNode(3)
    print(sol.right_side_view(root))  # Output: [1, 3, 7]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)
    print(sol.right_side_view(root))  # Output: [1, 2, 5, 7]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    print(sol.right_side_view(root))  # Output: [1, 2, 5, 6]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    print(sol.right_side_view(root))  # Output: [1, 2, 5]
    root = TreeNode(1)
    root.left = TreeNode
