class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix)==1 or len(matrix[0])==1:return True

        oli=[]
        status=1
        for i in matrix:
            if status:
                status=0
            elif not oli[:-1]==i[1:]:
                return False
            oli=i
        return True