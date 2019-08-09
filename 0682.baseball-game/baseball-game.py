class Solution:
    def calPoints(self, ops: List[str]) -> int:
        li=[]
        for i in ops:
            if i=="C":
                li.pop()
            elif i=="D":
                li.append(li[-1]*2)
            elif i=="+":
                li.append(sum(li[-2:]))
            else:
                li.append(int(i))
        return sum(li)