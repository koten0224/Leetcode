class Solution:
    def fib(self, N: int) -> int:
        if N==0:return 0
        elif N==1:return 1
        a,b=0,1
        for i in range(N-1):
            a,b=b,a+b
        return b