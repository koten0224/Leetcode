class Solution:
    def maxArea(self, height: List[int]) -> int:
        dic={index:value for index,value in enumerate(height)}
        j=len(height)-1
        i=0
        ans=0
        while j>i:
            a,b=dic[i],dic[j]
            w=j-i
            area=w*min(a,b)
            if area>ans:
                ans=area
            if a>b:
                j-=1
            else:
                i+=1
        return ans