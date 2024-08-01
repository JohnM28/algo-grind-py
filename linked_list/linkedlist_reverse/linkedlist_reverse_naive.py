from linked_list.linked_list_class import LinkedList


class LinkedListNaive(LinkedList):
    """
    Naive way to reverse a linkedlist
    """

    def reverse(self) -> LinkedList:
        """
        Naive way to reverse a linkedlist
        """
        reversed_linked_list = LinkedListNaive()
        current = self.head
        nodes = []
        while current:
            nodes.append(current.data)
            current = current.next

        for node in nodes[::-1]:
            reversed_linked_list.append(node)

        return reversed_linked_list


if __name__ == "__main__":
    values = [1, 4, 5, 6, 7, 2, 4, 20]
    linked_list = LinkedListNaive()
    for value in values:
        linked_list.append(value)
    linked_list_reversed = linked_list.reverse()
    print(linked_list)
    print(linked_list_reversed)
