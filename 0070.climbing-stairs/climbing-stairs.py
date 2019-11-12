class Solution:
    def climbStairs(self, n: int) -> int:
        if n<4:return n
        li=[1,2,3]
        for i in range(n-3):
            li.append(sum(li[-2:]))
        return li[-1]
        