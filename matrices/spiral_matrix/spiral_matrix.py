"""
Given an m×nm×n matrix, return an array containing the matrix elements in spiral order, starting from the top-left cell.

Constraints:
    1≤1≤ matrix.length ≤10≤10
    1≤1≤ matrix[i].length ≤10≤10
    −100≤−100≤ matrix[i][j] ≤100≤100
"""
from typing import List


class Solution:
    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        """
        Returns the matrix elements in spiral order
        :param matrix:
        :return:
        """
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while left <= right and top <= bottom:
            # top, far left to right
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1
            # far right, top to bottom
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1
            # bottom, right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            # far left, bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [1, 2, 3, 6, 9, 8, 7, 4, 5]
    print(s.spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))  # [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    print(s.spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))  # [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
    print(s.spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],
                          [13, 14, 15, 16]]))  # [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    print(s.spiral_order([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19,
                                                                                    20]]))  # [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
