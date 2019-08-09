class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        A = ['']
        for c in S:
            B = []
            if c.isdigit():
                for a in A:
                    B.append(a+c)
            else:
                for a in A:
                    B.append(a+c.lower())
                    B.append(a+c.upper())
            A=B
        return A