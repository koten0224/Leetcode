class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        li= [[x,y]for y in range(C) for x in range(R)]
        li.sort(key=lambda x:abs(r0-x[0])+abs(c0-x[1]))
        return li
        #return [[x,y] for y in range(C) for x in range(R)]