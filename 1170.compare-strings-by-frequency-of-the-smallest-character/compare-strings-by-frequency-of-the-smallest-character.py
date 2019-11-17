class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):return s.count(min(s))
        cq = [f(i) for i in queries]
        cw = collections.Counter(f(i) for i in words)
        
        return [sum(cw[y] for y in cw if x<y) for x in cq ]
        