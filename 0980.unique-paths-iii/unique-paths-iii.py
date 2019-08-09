
class Solution:
    def uniquePathsIII(self, grid):
        Y, X = len(grid), len(grid[0])
        startX, startY, numObs = 0, 0, 0
        self.ret, self.grid = 0, grid

        for y in range(Y):
            for x in range(X):
                if grid[y][x] == 1:
                    startX, startY = x, y
                elif grid[y][x] == -1:
                    numObs += 1

        def explore(x, y, steps):
            #print("x=%s y=%s steps=%s" % (x, y, steps))
            #for yy in range(Y):
            #    print(self.grid[yy])
            
            if grid[y][x] == 2:
                self.ret += 1 if numObs + steps == Y*X else 0    
                return
            
            self.grid[y][x] = -1
            if x > 0 and grid[y][x-1] >= 0:
                #print('Move Left')
                explore(x-1, y, steps + 1)
            if y > 0 and grid[y-1][x] >= 0:
                #print('Move Up')
                explore(x, y-1, steps + 1)
            if x < X-1 and grid[y][x+1] >= 0:
                #print('Move Right')
                explore(x+1, y, steps + 1)
            if y < Y-1 and grid[y+1][x] >= 0:
                #print('Move Down')
                explore(x, y+1, steps + 1)
            
            self.grid[y][x] = 0
        
        explore(startX, startY, 1)
        return self.ret