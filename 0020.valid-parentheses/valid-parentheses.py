class Solution:
    def isValid(self, s: str) -> bool:
        dic={"(":")","[":"]","{":"}"}
        if not s:return True
        if s[0] not in dic:return False
        temp=[]
        for i in s:
            if i not in dic:
                if temp and i==temp[-1]:temp.pop()
                else:return False
            else:temp.append(dic[i])
        return not temp