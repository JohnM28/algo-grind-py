"""
Given a string containing an arithmetic expression, implement a basic calculator that evaluates the expression string. The expression string can contain integer numeric values and should be able to handle the “+” and “-” operators, as well as “()” parentheses.

Constraints:

Let s be the expression string. We can assume the following constraints:

    1≤1≤ s.length ≤3×103≤3×103
    s consists of digits, “+”, “-”, “(”, and “)”.
    s represents a valid expression.
    “+” is not used as a unary operation ( +1+1 and +(2+3)+(2+3) are invalid).
    “-” could be used as a unary operation (−1−1 and −(2+3)−(2+3) are valid).
    There will be no two consecutive operators in the input.
    Every number and running calculation will fit in a signed 32-bit integer.
"""


class Calculator:
    """
    Basic calculator
    """
    def calculate(self, expression: str) -> int:
        """
        Calculate the expression
        """
        string_num = "0"
        sign = 1
        result = 0
        stack = []
        for c in expression:
            if c.isdigit():
                string_num += c
            if c in ["+", "-"]:
                result += int(string_num) * sign
                sign = -1 if c == "-" else 1
                string_num = "0"
            if c == "(":
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            if c == ")":
                result += int(string_num) * sign
                sign = stack.pop()
                result *= sign

                old_result = stack.pop()
                result += old_result
                string_num = "0"

        return result + int(string_num) * sign


if __name__ == "__main__":
    calc = Calculator()
    res = calc.calculate("-3+(5+5)+4")
    print(res)
