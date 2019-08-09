class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)   

        while A[0]>=A[1]+A[2]:

            if len(A)==3:
                
                return 0
            A.pop(0)
        return sum(A[:3])
            
            
            