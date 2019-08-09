"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        ar = '*'
        leng=len(grid)
        def nodeCreate(x=0,y=0,leng=leng):
            startVal=grid[x][y]
            check=1
            for row in grid[x:x+leng]:
                for col in row[y:y+leng]:
                    if col != startVal :
                        check=0
                        break
                if not check:break
            if check : return Node(bool(startVal),True,None,None,None,None)
            halfLeng=leng//2
            tl=nodeCreate(x,y,halfLeng)
            tr=nodeCreate(x,y+halfLeng,halfLeng)
            bl=nodeCreate(x+halfLeng,y,halfLeng)
            br=nodeCreate(x+halfLeng,y+halfLeng,halfLeng)
            node=Node(ar,False,tl,tr,bl,br)
            return node
        node=nodeCreate()
        return node
        