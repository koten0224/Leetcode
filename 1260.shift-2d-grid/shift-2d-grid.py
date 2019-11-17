class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r,c = len(grid),len(grid[0]) #get the nums of rows and columns
        temp=[j for i in grid for j in i] #make grid flatten
        temp=temp[-k%len(temp):]+temp[:-k%len(temp)] #do the shift
        return [[temp[i*c+j] for j in range(c)]for i in range(r)] #trans into grid