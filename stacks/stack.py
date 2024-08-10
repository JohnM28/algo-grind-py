"""
Stack implementation using list
"""


class Stack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self) -> bool:
        """
        Returns TRUE if the stack is empty. Otherwise FALSE
        :return:
        """
        return False if self.stack_list else True

    def top(self) -> int | None:
        """
        Returns the top element of the stack
        :return:
        """
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self) -> int:
        """
        Returns the size of the stack
        :return:
        """
        return len(self.stack_list)

    def push(self, value) -> None:
        """
        Pushes element at the top of the stack
        :param value:
        :return:
        """
        self.stack_list.append(value)

    def pop(self) -> int | None:
        """
        Removes and returns the top element of the stack
        :return:
        """
        if self.is_empty():
            return None
        return self.stack_list.pop()
