class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_pointer=l_pointer=ans=0
        for i in s:
            if i=="L":
                l_pointer+=1
            elif i=="R":
                r_pointer+=1
            if r_pointer==l_pointer:
                ans+=1
                r_pointer=l_pointer=0
        return ans
        