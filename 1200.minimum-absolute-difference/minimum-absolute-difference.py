class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        dic={}
        diff=10**6
        arr.sort()
        for i in range(len(arr)-1):
            temp=[arr[i],arr[i+1]]
            pre_diff=abs(temp[0]-temp[1])
            if pre_diff in dic:dic[pre_diff].append(temp)
            else:dic[pre_diff]=[temp]
            if pre_diff<diff:diff=pre_diff
        return dic[diff]