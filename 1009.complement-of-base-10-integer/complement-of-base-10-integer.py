class Solution:
    def bitwiseComplement(self, N: int) -> int:
        ans=bin(N)[2:].replace('1','2').replace('0','1').replace('2','0')
        return int(ans,2)