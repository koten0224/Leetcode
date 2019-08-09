class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generator(li='',zero=n,val=0):
            if zero==0:yield li+')'*val
            elif val>=0:
                yield from generator(li+'(',zero-1,val+1)
                yield from generator(li+')',zero,val-1)
        return [a for a in generator()]