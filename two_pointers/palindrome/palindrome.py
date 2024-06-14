def is_palindrome(string: str) -> bool:
    """
    This function checks if a string is a palindrome. It uses two pointers to compare the characters at the beginning and end of the string.
    """
    left = 0
    right = len(string) - 1
    while left <= right:
        if string[left] != string[right]:
            return False
        left = left + 1
        right = right - 1
    return True
