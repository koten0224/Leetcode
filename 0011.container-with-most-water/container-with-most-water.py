class Solution:
    def maxArea(self, height: List[int]) -> int:
        j=len(height)-1
        i=0
        ans=0
        while j>i:
            a,b=height[i],height[j]
            w=j-i
            area=w*min(a,b)
            if area>ans:
                ans=area
            if a>b:
                j-=1
            else:
                i+=1
        return ans
