from itertools import combinations as comb
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxArea = 0
        for i,j,k in comb(points,3):
            x1,y1 = i
            x2,y2 = j
            x3,y3 = k
            area = abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2
            if area > maxArea : maxArea = area
        return maxArea