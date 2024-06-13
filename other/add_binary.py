def reverse_and_order_strings(binary_string1: str, binary_string2: str) -> tuple:
    if len(binary_string1) >= len(binary_string2):
        long_str = binary_string1
        short_str = binary_string2
    else:
        long_str = binary_string2
        short_str = binary_string1

    return iter(long_str[::-1]), iter(short_str[::-1])


def add_binary(str1: str, str2: str) -> str:
    result = ""
    carry = 0
    first_str, second_str = reverse_and_order_strings(str1, str2)
    for first_binary in first_str:
        sec_binary = next(second_str, 0)
        binary_sum = int(first_binary) + int(sec_binary) + carry
        if binary_sum == 2:
            carry = 1
            result += "0"

        elif binary_sum == 3:
            carry = 1
            result += "1"

        else:
            carry = 0
            result += str(binary_sum)

    if carry != 0:
        result += str(carry)

    return result[::-1]
