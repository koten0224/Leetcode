class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a==b:return -1
        aleng = len(a)
        bleng = len(b)
        return max(aleng,bleng)