class Solution(object):
    def numSpecialEquivGroups(self, A):
        if len(A)==0 :return 0 
        if len(A[0])==0 :return 1
        if len(A[0])<3:return len(set(A))
        """
        :type A: List[str]
        :rtype: int
        """
        Set=set()
        
        for seq in A:
            seqList=[[],[]]
            for i in range(len(seq)):
                if i%2:seqList[1].append(seq[i])
                else:seqList[0].append(seq[i])
            seqList[0].sort()
            seqList[1].sort()
            seqList=','.join([''.join(seqList[0]),''.join(seqList[1])])
            Set.add(seqList)
        return len(Set)