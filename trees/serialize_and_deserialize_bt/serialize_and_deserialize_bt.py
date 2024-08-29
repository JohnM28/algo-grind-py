"""
Serialize a given binary tree to a file and deserialize it back to a tree. Make sure that the original and the deserialized trees are identical.

    Serialize: Write the tree to a file.

    Deserialize: Read from a file and reconstruct the tree in memory.

Serialize the tree into a list of integers, and then, deserialize it back from the list to a tree. For simplicity’s sake,
    there’s no need to write the list to the files.
"""
import json
from collections import deque
from trees.binary_tree import TreeNode
from typing import TextIO


class TreeSerializer:
    def serialize(self, root: TreeNode):
        """
        Serialize the given tree to a file.
        :param root:
        :return:
        """
        output = []
        self._bfs_traverse(root, output)
        # Remove trailing None values
        while output and output[-1] is None:
            output.pop()
        print(output)
        with open("serialized_data.txt", "w") as ser_file:
            ser_file.write(str(output).replace("None", "null"))

    def _bfs_traverse(self, root: TreeNode, output: list):
        """
        Perform a breadth-first traversal of the tree.
        :param root:
        :param output:
        :return:
        """
        if not root:
            return
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                output.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                output.append(None)

    def deserialize(self, data: str):
        """
        Deserialize the given data to a binary tree.
        :param data:
        :return:
        """
        tree_list = json.loads(data)
        if not tree_list:
            return None

        root = TreeNode(tree_list[0])
        queue = deque([root])
        i = 1
        while queue and i < len(tree_list):
            curr_node = queue.popleft()

            if i < len(tree_list) and tree_list[i] is not None:
                curr_node.left = TreeNode(tree_list[i])
                queue.append(curr_node.left)
            i += 1

            if i < len(tree_list) and tree_list[i] is not None:
                curr_node.right = TreeNode(tree_list[i])
                queue.append(curr_node.right)
            i += 1

        return root


if __name__ == "__main__":
    ser = TreeSerializer()
    root = ser.deserialize("[1,2,3,null,null,4,5]")
    ser.serialize(root)
    with open("serialized_data.txt", "r") as file:
        data = file.readline()
    root2 = ser.deserialize(data)
    ser.serialize(root2)
