class Solution:
    def canWinNim(self, n: int) -> bool:
        ans = bool(n%4)
        return ans