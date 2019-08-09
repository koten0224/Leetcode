class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        ans=0
        for row in grid:
            last=None
            for num in row:
                ans+=num*4
                if num:ans+=2
                if last:ans-=min(last,num)*2
                last=num
        for col in zip(*grid):
            last=None
            for num in col:
                if last:ans-=min(last,num)*2
                last=num
        return ans