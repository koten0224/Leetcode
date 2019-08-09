class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        if len(A)==0:return 0
        xlen,ylen=len(A[0]),len(A)
        count=0
        for x in range(xlen):
            for y in range(ylen-1):
                if A[y][x]>A[y+1][x]:
                    count+=1
                    break
        return count
        