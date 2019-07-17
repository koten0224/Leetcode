# -*- coding: utf-8 -*-

def runBoard(board,times=0,you_want_calculate_times = True): #遞迴檢測所用之函數
     #you_want_calculate_times控制是否統計運算次數並回傳

    def numInclude(inp_row,inp_col,board): #輸入座標，目前版面
        boardrow = board[inp_row] #定義檢測數值所在之橫列
        boardcolumn = [board[r][inp_col] for r in range(9)] #定義檢測數值所在之直欄
        row , col = inp_row//3*3 , inp_col//3*3
        boardsquare = [board[row+x][col+y]for x in range(3) for y in range(3)] #定義檢測數值所在之九宮格
        return set(boardrow + boardcolumn + boardsquare) #回傳列、欄、宮所有值
        
    possibleNum = [0]*9 #讓possiblenum原始長度為9以便進行長度比對
    row=col=None #先設定座標值為None供後續檢測
    for prow in range(9):
        for pcol in range(9):
            if not board[prow][pcol]:#如果有格子為0則進入
                area=numInclude(prow,pcol,board) #讀取列、欄、宮所有值
                possibleNum1 = [num for num in range(1,10) if not num in area] #過濾出此格的所有可能數字
                if not possibleNum1:return None,times #如果有格子填不下去了則退回一層
                if len(possibleNum1) < len(possibleNum) : #尋找可能性最少的格子
                    row,col,possibleNum = prow,pcol,possibleNum1
                    
    if row==col==None: #如果找不到空格(0)，在跑完9*9=81格後row and col依舊為None，這時就可以回傳答案了
        if you_want_calculate_times:
            return [[col for col in row]for row in board],times 
            #這樣寫是為了不用deepcopy達成deepcopy的效果，防止回傳的答案後面又全被改回0
        else:
            return [[col for col in row]for row in board]
            
    for fillNum in possibleNum: #由possibleNum讀取可能的數字
        board[row][col] = fillNum #填入可能數字
        #[print(''.join([str(i) for i in j])) for j in board]
        #預留監測運行過程用的CODE
        times += 1
        if you_want_calculate_times:
            answer , times = runBoard(board,times) #尋找下一個空格(0)繼續填入數字
        else:
            answer = runBoard(board)
        if answer : #如果answer有接收到回傳的LIST就把answer一層層回傳
            board[row][col] = 0 #把題目的list回歸原狀
            if you_want_calculate_times:
                return answer,times
            else:return answer
                
    #若後面的空格都檢查過，這邊跑完possibleNum也沒有答案，則此座標的數值歸0並退回一層
    board[row][col] = 0
    if you_want_calculate_times:return None,times
    else:return None
