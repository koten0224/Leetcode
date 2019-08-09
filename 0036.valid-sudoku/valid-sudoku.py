class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nine=range(9)
        three=range(3)
        for i in nine:
            setRow,setCol,setSquare = set() , set() , set()
            for num in board[i]:
                if num=='.':continue
                elif num in setRow:return False
                setRow.add(num)
            for num in [board[row][i] for row in nine]:
                if num=='.':continue
                elif num in setCol:return False
                setCol.add(num)
            for num in [board[i//3*3+x][i%3*3+y] for x in three for y in three]:
                if num=='.':continue
                elif num in setSquare:return False
                setSquare.add(num)
            
        
        
        
        return True