class Solution:

    def matrixScore(self, A: List[List[int]]) -> int:
        self.row = len(A)
        self.col = len(A[0])
        for i,row in enumerate(A):
            if row[0]==0:
                for x in range(self.col):
                    if A[i][x]==1:A[i][x]=0
                    else:A[i][x]=1
        for i,col in enumerate(zip(*A)):
            if col.count(1)<self.row/2:
                for x in range(self.row):
                    if A[x][i]==1:A[x][i]=0
                    else:A[x][i]=1
        return sum(2**a for i in A for a,b in enumerate(i[::-1]) if b)
