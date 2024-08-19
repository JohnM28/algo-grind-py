from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Traverse:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root:
            result.append(root.val)
            result.extend(self.preorderTraversal(root.left))
            result.extend(self.preorderTraversal(root.right))
        return result

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root:
            result.extend(self.inorderTraversal(root.left))
            result.append(root.val)
            result.extend(self.inorderTraversal(root.right))
        return result

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root:
            result.extend(self.postorderTraversal(root.left))
            result.extend(self.postorderTraversal(root.right))
            result.append(root.val)
        return result
