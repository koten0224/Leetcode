class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return [x for x in words if len(set(x))==len(set(pattern))==len(set(zip(x,pattern)))]