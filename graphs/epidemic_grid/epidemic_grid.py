"""
Problem Statement:
You are given a 2D grid representing a population. Each cell in the grid contains a positive integer representing the resistance power of a person.
A disease spreads from a person with higher resistance to an adjacent person with lower resistance (up, down, left, or right).
Given the position of a person initially infected by the disease, return the list of all infected positions in the order they get infected.
Example:
Input:
grid = [
  [5, 3, 4],
  [6, 1, 7],
  [2, 8, 9]
]
start = (1, 1)

Output:
[(1, 1), (1, 0), (0, 1)]
"""
from typing import Tuple
from collections import deque


class Epidemic:
    """
    a class to represent an epidemic in a grid of people with resistance power to a disease spreading from a person
        with higher resistance to an adjacent person with lower resistance
    """

    def find_infected(self, start: Tuple[int, int], grid) -> set:
        """
        Time complexity: O(m*n) where m is the number of rows and n is the number of columns in the grid
        """
        queue = deque([start])
        infected = {start}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, up, left, down
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in infected:
                    if grid[nx][ny] < grid[x][y]:
                        infected.add((nx, ny))
                        queue.append((nx, ny))

        return infected


if __name__ == "__main__":
    epidemic = Epidemic()
    grid = [
        [5, 3, 4],
        [6, 1, 7],
        [2, 8, 9]
    ]
    start = (0, 1)
    print(epidemic.find_infected(start, grid))
    grid = [
        [10, 3, 4],
        [6, 5, 7],
        [2, 8, 9]
    ]
    start = (1, 1)
    print(epidemic.find_infected(start, grid))
