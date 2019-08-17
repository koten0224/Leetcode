class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        grid = [[1]*m if i==0 else [1 if j==0 else 0 for j in range(m)] for i in range(n)]
        for y in range(1,n):
            for x in range(1,m):
                grid[y][x]=grid[y-1][x]+grid[y][x-1]
        return grid[-1][-1]
        '''
        
        return int(math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1)))
    