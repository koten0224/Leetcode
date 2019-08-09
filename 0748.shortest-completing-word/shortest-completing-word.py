class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = [sub.lower() for sub in licensePlate if sub.isalpha()]
        licenseDic = {}
        for sub in licensePlate:
            if sub in licenseDic:licenseDic[sub]+=1
            else:licenseDic[sub]=1
        minleng = 16
        minword = None
        for word in words:
            leng = len(word)
            wordDic = {}
            for sub in word:
                if sub in wordDic:wordDic[sub]+=1
                else:wordDic[sub]=1
            check = 1
            for sub,val in licenseDic.items():
                if sub in wordDic:
                    if val > wordDic[sub]:
                        check = 0
                        break
                else:check = 0
            if not check:continue
            if check:
                if leng < minleng:
                    minleng = leng
                    minword = word
        return minword