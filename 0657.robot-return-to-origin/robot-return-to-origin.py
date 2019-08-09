class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        coordinate=[0,0]
        movedic={"L":(-1,0),
                "R":(1,0),
                "U":(0,1),
                "D":(0,-1)}
        movelist=[movedic[i] for i in moves]
        for move in movelist:
            coordinate[0]+=move[0]
            coordinate[1]+=move[1]
        return coordinate==[0,0]
        