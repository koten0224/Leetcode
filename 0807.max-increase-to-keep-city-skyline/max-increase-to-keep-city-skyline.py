class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        leng = len(grid)
        rowsMax = [max(row) for row in grid]
        rang = range(leng)
        colsMax = [max(grid[row][col] for row in rang) for col in rang]
        ans = sum(min(rowsMax[row],colsMax[col]) - grid[row][col] for row in rang for col in rang)
        return ans
        