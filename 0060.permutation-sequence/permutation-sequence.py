class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = ''
        List = [str(i) for i in range(1,n+1)]
        while List:
            x = math.factorial(n-1)
            index = (k-1)//x
            string = List.pop(index)
            ans+=string
            n-=1
            k %= x
        return ans