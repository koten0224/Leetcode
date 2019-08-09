class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        checklist=list(A[0])
        for string in A[1:]:
            if not checklist:return []
            checklist1=[i for i in checklist]
            for letter in checklist:
                if checklist1.count(letter)>string.count(letter):
                    checklist1.remove(letter)
            checklist=checklist1
        return checklist