class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        sub=[sentence for sentence in logs if not sentence.split(' ')[-1].isdigit()]
        sub.sort(key=lambda x:x[x.index(' ')+1:]+x[:x.index(' ')])
        num=[sentence for sentence in logs if sentence.split(' ')[1].isdigit()]
        return sub+num