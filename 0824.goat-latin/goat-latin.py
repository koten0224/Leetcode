class Solution:
    def toGoatLatin(self, S: str) -> str:
        
        spl=S.split(' ')
        leng=len(spl)
        vowel=set('aeiouAEIOU')
        for i in range(leng):
            sub=spl[i]            
            if not sub[0] in vowel:
                sub=sub[1:]+sub[0]
            spl[i]=sub+'ma'+'a'*(i+1)
            
        ans=' '.join(spl)
        
        return ans