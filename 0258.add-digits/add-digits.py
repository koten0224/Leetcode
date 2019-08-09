class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:return num
        else: return self.addDigits(sum(int(n) for n in str(num)))