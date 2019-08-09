class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def runBoard(board): 
            def numInclude(inp_row,inp_col,board): 
                boardrow = board[inp_row] 
                boardcolumn = [board[0][inp_col],board[1][inp_col],board[2][inp_col],board[3][inp_col],board[4][inp_col],board[5][inp_col],board[6][inp_col],board[7][inp_col],board[8][inp_col] ]
                row , col = inp_row//3*3 , inp_col//3*3
                boardsquare = board[row+0][col:col+3]+\
                board[row+1][col:col+3]+\
                board[row+2][col:col+3] 
                return set(boardrow + boardcolumn + boardsquare) 
            possibleNum = [0]*9 
            row=col=None 
            for prow in range(9):
                for pcol in range(9):
                    if not board[prow][pcol]:
                        area=numInclude(prow,pcol,board) 
                        possibleNum1 = [num for num in range(1,10) if not num in area] 
                        if not possibleNum1:return
                        if len(possibleNum1) < len(possibleNum) : 
                            row,col,possibleNum = prow,pcol,possibleNum1
            if row==col==None: 
                return True
            for fillNum in possibleNum: 
                board[row][col] = fillNum 
                answer = runBoard(board)
                if answer :  
                    return True
            board[row][col] = 0
        for x in range(9):
            for y in range(9):
                num=board[x][y]
                if num.isdigit():board[x][y]=int(num)
                else:board[x][y]=0
        runBoard(board)
        for x in range(9):
            for y in range(9):
                board[x][y]=str(board[x][y])