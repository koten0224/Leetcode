class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        if len(A)<=1:return 0
        ans=max(A)-min(A)
        if ans<=K*2:return 0
        return ans-K*2
        
        
        