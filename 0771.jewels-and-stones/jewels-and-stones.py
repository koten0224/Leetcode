class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count=0
        for i in S:
            if i not in J:continue
            count+=1

        return count