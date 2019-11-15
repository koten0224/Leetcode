class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans=0
        chars_dic=collections.Counter(chars)
        for word in words:
            word_dic=collections.Counter(word)
            if all(i in chars_dic and word_dic[i] <= chars_dic[i] for i in word_dic):
                ans+=len(word)
        return ans