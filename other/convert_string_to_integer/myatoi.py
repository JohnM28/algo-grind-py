def remove_leading_space(input_string: str) -> str:
    """
    Remove leading white space from string
    """
    first_non_space_index = 0
    while first_non_space_index < len(input_string) and input_string[first_non_space_index] == ' ':
        first_non_space_index += 1
    return input_string[first_non_space_index:]


def myatoi(input_string: str) -> int:
    """
    This function converts a string to an integer. The function first removes leading spaces from the input string.
    Then it checks if the first character is '+' or '-', and sets the multiplier accordingly.
    It then iterates over the characters in the string, building the result as long as the characters are digits.
    If a non-digit character is encountered before any digit, the function returns 0.
    If a non-digit character is encountered after some digits, the function breaks the loop and proceeds to the next step.
    The function then converts the result string to an integer and multiplies it by the multiplier.
    If the final result is outside the range of a 32-bit signed integer, the function returns the maximum or minimum value.
    Otherwise, it returns the final result.
    """
    digit_found = False
    result = ""
    multiplier = 1
    input_string = remove_leading_space(input_string)

    if not input_string:
        return 0

    if input_string[0] in ["+", "-"]:
        multiplier = 1 if input_string[0] == "+" else -1
        input_string = input_string[1:]

    for char in input_string:
        if char.isdigit():
            result += char
            if not digit_found:
                digit_found = True
        elif not digit_found:
            return 0
        else:
            break

    if not result:
        return 0

    final_result = int(result) * multiplier
    if final_result > 2 ** 31 - 1:
        return 2 ** 31 - 1
    if final_result < -2 ** 31:
        return -2 ** 31
    return final_result
