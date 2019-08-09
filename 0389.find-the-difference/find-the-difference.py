from collections import Counter as counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = counter(s)
        b = counter(t)
        return ''.join((b-a).elements())