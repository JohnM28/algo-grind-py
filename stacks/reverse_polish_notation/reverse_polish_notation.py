"""
Given an arithmetic expression in a Reverse Polish Notation (RPN) as an array of strings, tokens, your task is to evaluate and return the value of the given expression.

Points to consider:

    Valid operators are +, -, *, and /.

    Each operand can be an integer or another expression.

    The division between two integers should truncate toward zero.

The given Reverse Polish Notation expression is guaranteed to be valid. This ensures that the expression always evaluates to a result and that there are no division-by-zero operations.

Constraints:
    1≤1≤ tokens.length ≤104≤104

    tokens[i] is either an operator (+, -, *, or /) or an integer in the range [−200,200][−200,200].
"""


class RPN:
    """
    Reverse Polish Notation (RPN) is a mathematical notation in which every operator follows all of its operands.
    """

    def rpn(self, tokens: list) -> int:
        """
        Evaluate the given expression
        """
        stack = []
        for t in tokens:
            match t:
                case "+":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a + b)
                case "-":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a - b)
                case "*":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a * b)
                case "/":
                    b, a = stack.pop(), stack.pop()
                    stack.append(int(a / b))
                case _:
                    stack.append(int(t))
        return stack.pop()


if __name__ == "__main__":
    rpn = RPN()
    tokens = ["5", "1", "2", "+", "4", "*", "+", "3", "-"]
    res = rpn.rpn(tokens)
    print(res)
