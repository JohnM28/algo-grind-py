"""
Problem Statement: Longest Substring with At Most K Distinct Characters

Given a string s and an integer k, you need to find the length of the longest substring of s that contains at most k distinct characters.

Example 1:
    Input: s = "eceba", k = 2
    Output: 3
    Explanation: The longest substring with at most 2 distinct characters is "ece", which has a length of 3.

Example 2:
    Input: s = "aa", k = 1
    Output: 2
    Explanation: The longest substring with at most 1 distinct character is "aa", which has a length of 2.
"""


class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        """
        Time complexity: O(n) where n is the length of the string s
        Space complexity: O(k) where k is the number of distinct characters in the string s
        """
        longest = 0
        s_freq = {}
        start = 0
        for end in range(len(s)):
            s_freq[s[end]] = s_freq.get(s[end], 0) + 1
            while len(s_freq) > k:
                s_freq[s[start]] = s_freq.get(s[start], 0) - 1
                if s_freq[s[start]] == 0:
                    del s_freq[s[start]]
                start += 1
            longest = max(longest, end - start + 1)

        return longest


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ("eceba", 2, 3),
        ("aa", 1, 2)
    ]

    for s, k, expected in test_cases:
        result = solution.length_of_longest_substring_k_distinct(s, k)
        print(f"length_of_longest_substring_k_distinct({s}, {k}) = {result}, expected = {expected}")
