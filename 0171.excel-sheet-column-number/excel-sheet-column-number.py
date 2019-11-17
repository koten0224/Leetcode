class Solution:
    def titleToNumber(self, s: str) -> int:
        return sum((ord(v)-64)*26**i for i,v in enumerate(s[::-1]))