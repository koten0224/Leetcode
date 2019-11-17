class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        r,c=len(image),len(image[0])
        fill_set=set()
        temp=set()
        fill_set.add((sr,sc))
        temp.add((sr,sc))
        color=image[sr][sc]
        while temp:
            print(temp)
            pre_temp=set()
            for x1,y1 in temp:
                for x,y in [(x1-1,y1),(x1+1,y1),(x1,y1+1),(x1,y1-1)]:
                    if r>x>=0 and c>y>=0 and (x,y) not in fill_set and image[x][y]==color:
                        pre_temp.add((x,y))
                        fill_set.add((x,y))
            temp=pre_temp
        for x,y in fill_set:image[x][y]=newColor
        return image
        
        