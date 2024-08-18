"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.
"""
from trees.binary_tree import TreeNode


class Solution:
    def has_path_sum(self, root: TreeNode | None, target_sum: int) -> bool:
        """
        Checks if the tree has a path sum equal to the target sum
        """
        if not root:
            return False
        return self._traverse_and_find(root, 0, target_sum)

    def _traverse_and_find(self, node: TreeNode, value_sum: int, target_sum: int) -> bool:
        """
        Traverses the tree and finds the path sum
        """
        if not node:
            return False
        value_sum += node.val
        if not node.left and not node.right:
            return value_sum == target_sum
        return self._traverse_and_find(node.left, value_sum, target_sum) or self._traverse_and_find(node.right,
                                                                                                    value_sum,
                                                                                                    target_sum)


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    target_sum = 22
    print(sol.has_path_sum(root, target_sum))
