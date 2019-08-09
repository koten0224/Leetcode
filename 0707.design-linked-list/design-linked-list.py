class MyLinkedList:

    def __init__(self):
        self.val=[]
        self.next=None
    def get(self, index: int) -> int:
        if index<0 or index>=len(self.val):return -1
        return self.val[index]
    def addAtHead(self, val: int) -> None:
        self.val=[val]+self.val
    def addAtTail(self, val: int) -> None:
        self.val.append(val)
    def addAtIndex(self, index: int, val: int) -> None:
        if index<-1 or index>len(self.val):return
        li=self.val
        self.val=li[:index]+[val]+li[index:]
    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=len(self.val):return
        del self.val[index]
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)