"""
Reverse a linkedlist in-place
optimization: O(1) space complexity
"""
from linked_list.linked_list_class import LinkedList, Node


class LinkedListOptimized(LinkedList):
    """
    Optimized way to reverse a linkedlist
    """

    def reverse(self) -> None:
        """
        Optimized way to reverse a linkedlist
        """
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


if __name__ == "__main__":
    values = [1, 4, 5, 6, 9, 7, 2, 4, 20]
    linked_list = LinkedListOptimized()
    for value in values:
        linked_list.append(value)
    linked_list.reverse()

    print(linked_list)
