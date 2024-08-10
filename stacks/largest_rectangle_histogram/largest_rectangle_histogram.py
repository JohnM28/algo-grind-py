"""
Statement

Given an array of integers, heights, that represents the heights of bars in a histogram, find the area of the largest rectangle in the histogram, where the rectangle has a constant width of 11 unit for each bar.
Constraints
    1≤1≤ heights.length ≤103≤103
    0≤0≤ heights[i] ≤104≤104
"""


class LargestRectangleHistogram:
    """
    Largest Rectangle in Histogram
    """

    def largest_rectangle_area_brute(self, heights: list) -> int:
        """
        Calculate the area of the largest rectangle in the histogram by brute force
        """
        max_area = 0
        n = len(heights)

        for left in range(n):
            for right in range(left, n):
                min_height: int = min(heights[left:right + 1])
                width = right - left + 1
                area = min_height * width
                max_area = max(max_area, area)

        return max_area

    def largest_rectangle_area_stack(self, heights: list) -> int:
        """
        TODO: Solve it using stack
        Calculate the area of the largest rectangle in the histogram using stack
        """
        pass


if __name__ == "__main__":
    lrh = LargestRectangleHistogram()
    heights = [2, 1, 5, 6, 2, 3]
    res = lrh.largest_rectangle_area_brute(heights)
    print(res)
    heights = [2, 4]
    res = lrh.largest_rectangle_area_brute(heights)
    print(res)
    heights = [2, 4, 5, 7, 3, 9]
    res = lrh.largest_rectangle_area_brute(heights)
    print(res)
