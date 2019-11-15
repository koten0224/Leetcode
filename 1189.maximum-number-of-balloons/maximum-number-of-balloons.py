class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic=collections.Counter(text+"balon")
        dic.subtract("balon")
        return min(dic[x]//2 if x in "lo" else dic[x] for x in "balon")
        