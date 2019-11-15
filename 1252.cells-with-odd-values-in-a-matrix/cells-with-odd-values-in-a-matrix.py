class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        ans=0
        r_dic=[0 for i in range(n)]
        c_dic=[0 for i in range(m)]
        for i in indices:
            r_dic[i[0]]+=1
            c_dic[i[1]]+=1
        for i in r_dic:
            
            for j in c_dic:
                if i%2!=j%2:ans+=1
        return ans