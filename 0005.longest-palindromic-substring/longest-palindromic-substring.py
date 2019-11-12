class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:return ''
        index_dic = {}
        ans=s[0]
        for index in range(len(s)):
            letter = s[index]
            if letter in index_dic:
                for index2 in index_dic[letter]:
                    pre_palin = s[index2:index+1]
                    if len(pre_palin)<=len(ans):break
                    if pre_palin==pre_palin[::-1]:
                        ans=pre_palin
                        break
                index_dic[letter].append(index)
            else:index_dic[letter]=[index]
        return ans