class Solution:
    def reverseWords(self, s: str) -> str:
        s=' '.join([''.join(i) for i in [list(i)[-1::-1] for i in s.split(' ')]])
        return s