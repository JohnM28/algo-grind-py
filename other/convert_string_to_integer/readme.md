# Statement

Write a function, myAtoi(string s), that converts a string to a 32–bit signed integer. It is equivalent to the atoi function in C/C++.

The myAtoi function reads the input string, s, from left to right for the conversion process. The conversion begins by removing any leading whitespace. Then, it checks if the next character is '+' or '-'. If it's '-', it implies that the result is negative, and there must be a '-' sign in front of the resulting integer. Otherwise, '+' implies that the result is positive, so there is no need to add a '+' sign in front of the resulting integer. For example, "-2525" converts to -2525, and "+9191" converts to 9191. However, if neither is present, assume the result is positive.

After removing the whitespace, if the first non-space character is not a sign character, '+' or '-', but a non-digit character, i.e., an English letter or the period '..', the function stops processing further and returns 00. For example, the strings "   One11" and "   .5.5" convert to 00. Additionally, if the first non-space character is a sign character, '+' or '-', and the next character is a non-digit character (including the space character), the function returns 00. For example, the strings "   +.23.23" , "   -  4949", and "   +R345345" convert to 00.

The function continues to read the string while checking if the subsequent character is a digit and stops reading when a non-digit character is encountered. For characters that are digits, the function concatenates them. Next, it transforms the collected digits into their corresponding integer value. It ensures that the sign value, if any, is adjusted to the resulting integer. For example, "33" transforms to 33, "00450045" changes to 4545, "-88" results in -88 and "+640640" becomes 640640. The second example implies that there is no need to add any leading zeros in the final answer.

Finally, the function checks if the resulting integer goes out of the range of a 32–bit signed integer, [[-231231, 231231 - 1]1]. It returns -231231 if it's less than -231231 and returns 231−1231−1 if it's greater than 231−1231−1. Otherwise, if the resulting integer is within the defined range, return it as the final output.

    Note: The space character (' ') and the period ('..') are part of the non-digit characters. Therefore, they will get ignored and won't affect the final answer. For example, "7  9  0790" converts to 77 and "85.985.9" converts to 8585.

Constraints:

    0≤0≤ s.length ≤200≤200

    The string s may have:

        digit characters from 00–99.

        non-digit characters, including lower-case and upper-case English letters, space character (' '), period ('..'), and sign characters ('+' and '-').