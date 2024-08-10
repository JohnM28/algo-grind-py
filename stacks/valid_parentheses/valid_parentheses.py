"""
Statement

Given a string that may consist of opening and closing parentheses, your task is to check whether or not the string contains valid parenthesization.

The conditions to validate are as follows:

    Every opening parenthesis should be closed by the same kind of parenthesis. Therefore, {)and [(]) strings are invalid.

    Every opening parenthesis must be closed in the correct order. Therefore, )( and ()(() are invalid.

Constraints:

    1≤1≤ s.length ≤103≤103
    The string will only contain the following characters: (, ), [, ], { and }.
"""


class ValidParanthesis:
    PMAP = {
        "}": "{",
        "]": "[",
        ")": "("
    }

    def is_valid(self, s: str) -> bool:
        """
        Checks if the string contains valid paranthesis
        :param s:
        :return:
        """
        stack = []
        for c in s:
            if c not in self.PMAP:
                stack.append(c)
            else:
                if not stack or self.PMAP[c] != stack.pop():
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    vp = ValidParanthesis()
    assert vp.is_valid("()") == True
    assert vp.is_valid("()[]{}") == True
    assert vp.is_valid("(]") == False
    assert vp.is_valid("([)]") == False
    assert vp.is_valid("{[]}") == True
    assert vp.is_valid("}") == False
