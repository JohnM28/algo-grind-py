"""
Statement

Design a custom queue, MyQueue, using only two stacks. Implement the Push(), Pop(), Peek(), and Empty() methods:

    Void Push(int x): Pushes element at the end of the queue.
    Int Pop(): Removes and returns the element from the front of the queue.
    Int Peek(): Returns the element at the front of the queue.
    Boolean Empty(): Returns TRUE if the queue is empty. Otherwise FALSE.

You are required to only use the standard stack operations, which means that only the Push() to top, Peek() and Pop() from the top, Size(), and Is Empty() operations are valid.
Constraints:

    1<=1<= x <=100<=100
    A maximum of 100100 calls can be made to Push(), Pop(), Peek(), and Empty().
    The Pop() and Peek() methods will always be called on non-empty stacks.
"""
from stacks.stack import Stack


class MyQueue:
    """
    Custom queue implementation using two stacks
    """

    def __init__(self):
        self.stack = Stack()
        self.temp_stack = Stack()

    def push(self, x: int) -> None:
        """
        Pushes element at the end of the queue
        :param x:
        :return:
        """
        while not self.stack.is_empty():
            self.temp_stack.push(self.stack.pop())

        self.stack.push(x)

        while not self.temp_stack.is_empty():
            self.stack.push(self.temp_stack.pop())

    def pop(self) -> int | None:
        """
        Removes and returns the element from the front of the queue
        :return:
        """
        if self.stack:
            return self.stack.pop()
        return None

    def peek(self) -> int | None:
        """
        Returns the element at the front of the queue
        :return:
        """

        return self.stack.top()

    def empty(self) -> bool:
        """
        Returns TRUE if the queue is empty. Otherwise FALSE
        :return:
        """
        return self.stack.is_empty()


if __name__ == "__main__":
    queue = MyQueue()
    queue.push(3)
    queue.push(12)
    queue.push(1)
    queue.push(65)
    print(queue.peek())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.empty())
