class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return len([i for j in grid for i in j if i])+\
        sum([max(row) for row in grid])+\
        sum([max([grid[row][col] for row in range(len(grid))]) for col in range(len(grid[0]))])