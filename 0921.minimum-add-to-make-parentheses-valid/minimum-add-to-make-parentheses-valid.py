class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        dic = {'(':1,')':-1}
        val = 0
        count = 0
        for i in S:
            val += dic[i]
            if val<0:
                count +=1
                val = 0
        return val+count