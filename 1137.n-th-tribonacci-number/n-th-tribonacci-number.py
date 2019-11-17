class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c=0,1,1
        if n<3:return (a,b,c)[n]
        for _ in range(2,n):
            a,b,c=b,c,a+b+c
        return c