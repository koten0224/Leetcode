class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        oddl=[i for i in A if i%2]
        evenl=[i for i in A if not i%2]
        answer=[]
        for i in range(len(oddl)):
            answer.append(evenl.pop())
            answer.append(oddl.pop())
        return answer