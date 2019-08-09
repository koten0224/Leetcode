class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            if 'R' in board[i]: rc=(i,board[i].index('R'))
        row=board[rc[0]]
        row1=row[:rc[1]+1]
        row1.reverse()
        row2=row[rc[1]:]
        col=[board[x][rc[1]] for x in range(8)]
        col1=col[:rc[0]+1]
        col1.reverse()
        col2=col[rc[0]:]
        def check(li):
            if 'p' in li:
                if 'B' in li and li.index('B')<li.index('p'):return
                else:return 1
        return [check(li) for li in [row1,row2,col1,col2]].count(1)
        