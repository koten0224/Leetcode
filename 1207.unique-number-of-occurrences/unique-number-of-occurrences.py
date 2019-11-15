class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c=collections.Counter
        return c(c(arr).values()).most_common(1)[0][1]==1