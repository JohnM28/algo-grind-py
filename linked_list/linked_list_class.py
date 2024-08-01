"""
Linkedlist Base class structure
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def append(self, data) -> None:
        """
        Append a new node to the linkedlist
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current: Node = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data) -> None:
        """
        Prepend a new node to the linkedlist
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def __str__(self) -> str:
        result = ""
        current = self.head
        while current:
            result += str(current.data) + " -> "
            current = current.next
        result += "None"  # Append "None" to the end
        return result


if __name__ == "__main__":
    values = [1, 4, 5, 6, 7, 2, 4, 20]
    linked_list = LinkedList()
    for value in values:
        linked_list.append(value)
    print(linked_list)
