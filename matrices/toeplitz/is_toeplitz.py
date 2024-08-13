"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
"""
from typing import List


class Solution:
    def is_toeplitz_matrix(self, matrix: List[List[int]]) -> bool:
        """
        Returns TRUE if the matrix is Toeplitz. Otherwise FALSE
        """
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[i]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.is_toeplitz_matrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))  # True
    print(s.is_toeplitz_matrix([[1, 2], [2, 2]]))  # False
    print(s.is_toeplitz_matrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2], [1, 9, 5, 1]]))  # True
