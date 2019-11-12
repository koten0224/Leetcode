class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:return ""
        ans=strs[0]
        for word in strs[1:]:
            pre_ans=''
            for a,b in zip(ans,word):
                if a==b:
                    pre_ans+=a
                else:break
            ans=pre_ans
            if not ans:break
        return ans
