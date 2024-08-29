from typing import List

from trees.binary_tree import TreeNode


class Traverse:

    def dfs_preorder(self, root: TreeNode, output: list) -> list:
        if not root:
            return output
        output.append(root.val)
        self.dfs_preorder(root.left, output)
        self.dfs_preorder(root.right, output)
        return output

    def dfs_inorder(self, root: TreeNode, output: list) -> list:
        if not root:
            return output
        self.dfs_inorder(root.left, output)
        output.append(root.val)
        self.dfs_inorder(root.right, output)
        return output

    def dfs_postorder(self, root: TreeNode, output: list) -> list:
        if not root:
            return output
        self.dfs_postorder(root.left, output)
        self.dfs_postorder(root.right, output)
        output.append(root.val)
        return output


class Traverse2:
    def dfs_preorder(self, root: TreeNode) -> List[int]:
        result = []
        if root:
            result.append(root.val)
            result.extend(self.dfs_preorder(root.left))
            result.extend(self.dfs_preorder(root.right))
        return result

    def dfs_inorder(self, root: TreeNode) -> List[int]:
        result = []
        if root:
            result.extend(self.dfs_inorder(root.left))
            result.append(root.val)
            result.extend(self.dfs_inorder(root.right))
        return result

    def dfs_postorder(self, root: TreeNode) -> List[int]:
        result = []
        if root:
            result.extend(self.dfs_postorder(root.left))
            result.extend(self.dfs_postorder(root.right))
            result.append(root.val)
        return result
