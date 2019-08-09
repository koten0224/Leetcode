class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #if len(grid)==1:
            #if len(grid[0])==1:return grid[0][0]*4
            
        xlen=len(grid[0])
        ylen=len(grid)
        ans=sum(grid[0]+grid[-1]+[grid[i][0] for i in range(ylen)]+[grid[i][-1] for i in range(ylen)])
        def findZero(row,col):
            result=0
            coordinate=[[],[]]
            if not row and row<ylen-1:coordinate[0].append(row+1)
            elif row==ylen-1:coordinate[0].append(row-1)
            else: 
                coordinate[0].append(row+1)
                coordinate[0].append(row-1)
            if not col and col<xlen-1:coordinate[1].append(col+1)
            elif col==xlen-1:coordinate[1].append(col-1)
            else: 
                coordinate[1].append(col+1)
                coordinate[1].append(col-1)
            
            for i in coordinate[0]:
                if not grid[i][col]:result+=1
            for i in coordinate[1]:
                if not grid[row][i]:result+=1
            return result
        for y in range(ylen):
            
            for x in range(xlen):
                if grid[y][x]:ans+=findZero(y,x)
        return ans
            