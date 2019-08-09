class Solution:
    def reverse(self, x: int) -> int:
        
        y=x
        
        y=[i for i in str(y) if i.isdigit()]
        y.reverse()
        y=int(''.join(y))
        if x < 0 : y=-y
        if not (-(2**31) < y <(2**31-1)):return 0
        return y