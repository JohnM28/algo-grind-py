from collections import deque

from trees.binary_tree import TreeNode


class Traverse:
    def bfs(self, root: TreeNode) -> list[int]:
        result = []
        if not root:
            return result

        queue = deque([root])

        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    traverse = Traverse()
    print(traverse.bfs(root))  # Output: [1, 2, 3, 4, 5, 6, 7]
    print(traverse.bfs(None))  # Output: []